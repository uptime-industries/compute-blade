# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_emc2101.emc2101_lut`
================================================================================

Brushless fan controller: extended functionality


* Author(s): Bryan Siepert, Ryan Pavlik

Implementation Notes
--------------------

**Hardware:**

* `Adafruit EMC2101 Breakout <https://adafruit.com/product/4808>`_ (Product ID: 4808)

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

* Adafruit's Bus Device library:
  https://github.com/adafruit/Adafruit_CircuitPython_BusDevice

* Adafruit's Register library:
  https://github.com/adafruit/Adafruit_CircuitPython_Register


The class defined here may be used instead of :class:`adafruit_emc2101.EMC2101`,
if your device has enough RAM to support it. This class adds LUT control
and PWM frequency control to the base feature set.
"""

from micropython import const
from adafruit_register.i2c_struct_array import StructArray
from adafruit_register.i2c_struct import UnaryStruct
from adafruit_register.i2c_bit import RWBit
from adafruit_register.i2c_bits import RWBits
from . import EMC2101

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_EMC2101.git"

_FAN_CONFIG = const(0x4A)
_PWM_FREQ = const(0x4D)
_PWM_DIV = const(0x4E)
_LUT_HYSTERESIS = const(0x4F)
_LUT_BASE = const(0x50)

MAX_LUT_SPEED = 0x3F  # 6-bit value
MAX_LUT_TEMP = 0x7F  # 7-bit


def _speed_to_lsb(percentage):
    return round((percentage / 100.0) * MAX_LUT_SPEED)


class FanSpeedLUT:
    """A class used to provide a dict-like interface to the EMC2101's Temperature to Fan speed
    Look Up Table.

    Keys are integer temperatures, values are fan duty cycles between 0 and 100.
    A max of 8 values may be stored.

    To remove a single stored point in the LUT, assign it as `None`.
    """

    # 8 (Temperature, Speed) pairs in increasing order
    _fan_lut = StructArray(_LUT_BASE, "<B", 16)

    def __init__(self, fan_obj):
        self.emc_fan = fan_obj
        self.lut_values = {}
        self.i2c_device = fan_obj.i2c_device

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise IndexError
        if not index in self.lut_values:
            raise IndexError
        return self.lut_values[index]

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise IndexError
        if value is None:
            # Assign None to remove this entry
            del self.lut_values[index]
        elif value > 100.0 or value < 0:
            # Range check
            raise AttributeError("LUT values must be a fan speed from 0-100%")
        else:
            self.lut_values[index] = value
        self._update_lut()

    def __repr__(self):
        """return the official string representation of the LUT"""
        return "FanSpeedLUT <%x>" % id(self)

    def __str__(self):
        """return the official string representation of the LUT"""
        value_strs = []
        lut_keys = tuple(sorted(self.lut_values.keys()))
        for temp in lut_keys:
            fan_drive = self.lut_values[temp]
            value_strs.append("%d deg C => %.1f%% duty cycle" % (temp, fan_drive))

        return "\n".join(value_strs)

    def __len__(self):
        return len(self.lut_values)

    # this function does a whole lot of work to organized the user-supplied lut dict into
    # their correct spot within the lut table as pairs of set registers, sorted with the lowest
    # temperature first

    def _update_lut(self):
        # Make sure we're not going to try to set more entries than we have slots
        if len(self.lut_values) > 8:
            raise AttributeError("LUT can only contain a maximum of 8 items")

        # Backup state
        current_mode = self.emc_fan.lut_enabled

        # Disable the lut to allow it to be updated
        self.emc_fan.lut_enabled = False

        # we want to assign the lowest temperature to the lowest LUT slot, so we sort the keys/temps
        # get and sort the new lut keys so that we can assign them in order
        for idx, current_temp in enumerate(sorted(self.lut_values.keys())):
            current_speed = _speed_to_lsb(self.lut_values[current_temp])
            self._set_lut_entry(idx, current_temp, current_speed)

        # Set the remaining LUT entries to the default (Temp/Speed = max value)
        for idx in range(len(self.lut_values), 8):
            self._set_lut_entry(idx, MAX_LUT_TEMP, MAX_LUT_SPEED)
        self.emc_fan.lut_enabled = current_mode

    def _set_lut_entry(self, idx, temp, speed):
        self._fan_lut[idx * 2] = bytearray((temp,))
        self._fan_lut[idx * 2 + 1] = bytearray((speed,))


class EMC2101_LUT(EMC2101):  # pylint: disable=too-many-instance-attributes
    """Driver for the EMC2101 Fan Controller, with PWM frequency and LUT control.

    See :class:`adafruit_emc2101.EMC2101` for the base/common functionality.

    :param ~busio.I2C i2c_bus: The I2C bus the EMC is connected to.
    """

    _fan_pwm_clock_select = RWBit(_FAN_CONFIG, 3)
    _fan_pwm_clock_override = RWBit(_FAN_CONFIG, 2)
    _pwm_freq = RWBits(5, _PWM_FREQ, 0)
    _pwm_freq_div = UnaryStruct(_PWM_DIV, "<B")

    lut_temperature_hysteresis = UnaryStruct(_LUT_HYSTERESIS, "<B")
    """The amount of hysteresis in Degrees Celsius of hysteresis applied to temperature readings
    used for the LUT. As the temperature drops, the controller will switch to a lower LUT entry when
    the measured value is below the lower entry's threshold, minus the hysteresis value"""

    def __init__(self, i2c_bus):
        super().__init__(i2c_bus)

        self.initialize()
        self._lut = FanSpeedLUT(self)

    def initialize(self):
        """Reset the controller to an initial default configuration"""
        self.lut_enabled = False
        self._fan_pwm_clock_override = True
        super().initialize()

    def set_pwm_clock(self, use_preset=False, use_slow=False):
        """
             Select the PWM clock source, choosing between two preset clocks or by configuring the
             clock using `pwm_frequency` and `pwm_frequency_divisor`.

        :param bool use_preset:
         True: Select between two preset clock sources
         False: The PWM clock is set by `pwm_frequency` and `pwm_frequency_divisor`
        :param bool use_slow:
             True: Use the 1.4kHz clock
             False: Use the 360kHz clock.
        :type priority: integer or None
        :return: None
        :raises AttributeError: if use_preset is not a `bool`
        :raises AttributeError: if use_slow is not a `bool`

        """

        if not isinstance(use_preset, bool):
            raise AttributeError("use_preset must be given a bool")
        if not isinstance(use_slow, bool):
            raise AttributeError("use_slow_pwm must be given a bool")

        self._fan_pwm_clock_override = not use_preset
        self._fan_pwm_clock_select = use_slow

    @property
    def pwm_frequency(self):
        """Selects the base clock frequency used for the fan PWM output"""
        return self._pwm_freq

    @pwm_frequency.setter
    def pwm_frequency(self, value):
        if value < 0 or value > 0x1F:
            raise AttributeError("pwm_frequency must be from 0-31")
        self._pwm_freq_div = value

    @property
    def pwm_frequency_divisor(self):
        """The Divisor applied to the PWM frequency to set the final frequency"""
        return self._pwm_freq_div

    @pwm_frequency_divisor.setter
    def pwm_frequency_divisor(self, divisor):
        if divisor < 0 or divisor > 255:
            raise AttributeError("pwm_frequency_divisor must be from 0-255")
        self._pwm_freq_div = divisor

    @property
    def lut_enabled(self):
        """Enable or disable the internal look up table used to map a given temperature
        to a fan speed. When the LUT is disabled fan speed can be changed with `manual_fan_speed`"""
        return not self._fan_lut_prog

    @lut_enabled.setter
    def lut_enabled(self, enable_lut):
        self._fan_lut_prog = not enable_lut

    @property
    def lut(self):
        """The dict-like representation of the LUT, actually of type :class:`FanSpeedLUT`"""
        return self._lut
