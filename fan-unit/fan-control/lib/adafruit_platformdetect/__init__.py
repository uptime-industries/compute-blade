# Copyright (c) 2014-2018 Adafruit Industries
# Author: Tony DiCola, Limor Fried, Brennen Bearnes

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Attempt to detect the current platform.
"""
import re

from adafruit_platformdetect.board import Board
from adafruit_platformdetect.chip import Chip


# Various methods here may retain state in future, so tell pylint not to worry
# that they don't use self right now:
# pylint: disable=no-self-use
class Detector:
    """Wrap various platform detection functions."""

    def __init__(self):
        self.board = Board(self)
        self.chip = Chip(self)

    def get_cpuinfo_field(self, field):
        """
        Search /proc/cpuinfo for a field and return its value, if found,
        otherwise None.
        """
        # Match a line like 'Hardware   : BCM2709':
        pattern = r"^" + field + r"\s+:\s+(.*)$"

        with open("/proc/cpuinfo", "r") as infile:
            cpuinfo = infile.read().split("\n")
        for line in cpuinfo:
            match = re.search(pattern, line, flags=re.IGNORECASE)
            if match:
                return match.group(1)
        return None

    def check_dt_compatible_value(self, value):
        """
        Search /proc/device-tree/compatible for a value and return True, if found,
        otherwise False.
        """
        # Match a value like 'qcom,apq8016-sbc':
        dt_compatible = self.get_device_compatible()
        if dt_compatible and value in dt_compatible:
            return True

        return False

    def get_armbian_release_field(self, field):
        """
        Search /etc/armbian-release, if it exists, for a field and return its
        value, if found, otherwise None.
        """
        field_value = None

        pattern = r"^" + field + r"=(.*)"
        try:
            with open("/etc/armbian-release", "r") as release_file:
                armbian = release_file.read().split("\n")
                for line in armbian:
                    match = re.search(pattern, line)
                    if match:
                        field_value = match.group(1)
        except FileNotFoundError:
            pass

        return field_value

    def get_device_model(self):
        """
        Search /proc/device-tree/model for the device model and return its value, if found,
        otherwise None.
        """
        try:
            with open("/proc/device-tree/model", "r") as model_file:
                return model_file.read()
        except FileNotFoundError:
            pass
        return None

    def get_device_compatible(self):
        """
        Search /proc/device-tree/compatible for the compatible chip name.
        """
        try:
            with open("/proc/device-tree/compatible", "r") as model_file:
                return model_file.read()
        except FileNotFoundError:
            pass
        return None

    def check_board_asset_tag_value(self):
        """
        Search /sys/devices/virtual/dmi/id for the device model and return its value, if found,
        otherwise None.
        """
        try:
            with open("/sys/devices/virtual/dmi/id/board_asset_tag", "r") as tag_file:
                return tag_file.read().strip()
        except FileNotFoundError:
            pass
        return None

    def check_board_name_value(self):
        """
        Search /sys/devices/virtual/dmi/id for the board name and return its value, if found,
        otherwise None. Debian/ubuntu based
        """
        try:
            with open("/sys/devices/virtual/dmi/id/board_name", "r") as board_name_file:
                return board_name_file.read().strip()
        except FileNotFoundError:
            pass
        return None
