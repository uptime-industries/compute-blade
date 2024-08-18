# Changelog

## V1.0 MK4

![Blade-MK4-k with TPM highlighted](/img/blade/mk4-k-tpm.png)

### Improvements

- New TPM 2.0 module: [OPTIGA TPM SLB 9672](https://www.infineon.com/dgdl/Infineon-OPTIGA+TPM+SLB+9672+FW16-DataSheet-v01_00-EN.pdf?fileId=8ac78c8c7f2a768a017f899f82094435) as an upgrade of the previous generation

## V1.0 MK4-K

![Blade-MK4-k with power and UART and Exspaition pins highlighted](/img/blade/mk4-k-power.png)

### Improvements

- Increased power on the 3.3V bus to 16.5W. Which will allow the use of future high-speed modules
- Added overload and short circuit protection to the 5V and 3.3V outputs on the board
- The possibility of powering the blade from the 5V pin has been removed
- Power Good LED on the board works even without the Compute Module
- The low-speed modules connection is turned 180°

### Fixes

- The blue digital LED  would light up sometimes on startup due to power interference. Added additional filtering to the diode signal line, and the problem was solved
- A certain number of devices from early v1 batches may experience a voltage surge at startup under certain conditions. In extreme cases, this could potentially destroy the device’s components. In cooperation with the manufacturer of the PoE module, additional stabilization of the PoE module output completely eliminated the problem

## V1.0 MK1

![MK1 Dev Blade](/img/blade/mk1-dev.png)

### Improvements

- Increased standoffs height for CM4 allows you to use different clones without worrying about the space under the module;
- Power over Ethernet IEEE 802.3at (PoE+) up to 30W (normal operation 2-8W);
- New PoE module ([Silvertel AG5405](https://silvertel.com/images/datasheets/Ag5400-datasheet-high%20Efficiency-30W-Power-Over-Ethernet-Plus-Module-PoE+PD.pdf)) with one of the best characteristics in class
- Modified latch mounting holes for easier installation;
- More test points added

## V0.9 RC2
![RC2 blade](/img/blade/rc2.png)

### Features
- Support all Raspberry Pi CM4
- NVMe SSD up to 22110 (2230, 2242, 2260, 2280 supported)
- Gigabit Ethernet
- Power over Ethernet IEEE 802.3at (PoE+) up to 22W (normal operation 2-8W)
- Optional real-time clock (RTC) module
- Optional Zymbit ZYMKEY4i, or custom module for Zymbit Hardware Security(HSM)
- USB-A for a flash drive for copying data during setup with UART or YubiKey keys during operation
- MicroSD card port
- UART0 on the front (TX, RX, GND)
- Additional UART0 with 5v in (or out) next to RTC port
- Two digital RGB LEDs
- Hardware switchable WiFi, BT, and EEPROM write-protection
- Activity, Power, and SSD LEDs
- HDMI port for monitor (up to 4k60)
- USB-C port and PRIBOOT button to flash the bootloader, access to eMMC/SD card or tests
- TPM 2.0 onboard
- PWM fan connector for the custom backplane (Fan Units), supports UART communication
- Switchable USB input (USB-A or USB-C)
- Programmable button on the front panel
- Officially “Powered by Raspberry Pi”
- FCC and CE ready
- Individual serial number
- The power supply of the Raspberry Pi CM4 is now 5.1V, which has improved stability under overclocking. This is fully within the specifications (4.75V-5.25V)
- IEEE 802.3at detection (on Raspberry Pi with GPIO pin and additional LED on the blade)
- New button for the front panel (to feel the click better)
- All front LEDs can be turned off (except for Ethernet, this needs to be corrected in v.1), a very handy feature!
- Signed by [Ivan Kuleshov](https://www.linkedin.com/in/merocle/)