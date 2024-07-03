---
sidebar_position: 1
---
# Getting Started

## Prerequisites

---

Before beginning you will need the following items:

- Internet Connection
- [Raspberry Pi Compute Module 4](https://www.raspberrypi.com/products/compute-module-4) recommended SKU(CM4008000)
- Dev Compute Blade
- **USB-C cable,** Which can be connected to the your computer
- **USB-to-NVMe,** Such as [Ugreen M.2 NVMe SSD Enclosure Adapter](https://www.ugreen.com/products/ugreen-m-2-nvme-ssd-enclosure-adapter)
- **NVMe SSD**, Check our list of validated Drives if you are unsure which to get
- **PoE Power Delivery**, Capable of `802.3af`(PoE), `802.3at`(PoE+), or `802.3bt`(PoE++)
<!-- rewirte power requirments later USB C -->

Additionally make sure to have the following Software install on another computer:

- [Raspberry Pi Imager](https://github.com/raspberrypi/rpi-imager)
- [usbboot](https://github.com/raspberrypi/usbboot)

## Installing Ubuntu on the SSD

---

1. Install the NVMe SSD in to your USB-to-NVMe Adapter and plug it into your Computer
2. Using Raspberry Pi Imager 
    1. Select Device `Raspberry Pi 4`
    2. Select Operating System `Other general-purpose OS`>`Ubuntu`> `Ubuntu Server 24.04 LTS (64-bit)`
    3. For Storage select the SSD
    4. Then Click Next
3. Before RPI Imager will image your SSD it will ask “Would you like to apply OS customizations settings?” Click “Edit Settings”. 
    1. Set your `hostname`. We will use this to connect to you blade over SSH
    2. Set your `username` and `password`. We will us these to authenticate with SSH
    3. And Set you `locale`. This will make sure dates are displayed correctly for you
    4. Enable SSH. Under the “Services” tab Enable SSH with Password authentication
        1. Optionally, you could “Allow public-key authentication only” and add a Public key
4. Once your settings are configured you may continue to image your SSD
5. Final, RPI Imager will tell you that is has installed the image on the SSD and it is safe to removed. Unplug the USB-to-NVMe Adapter and remove the SSD from the adapter.

## Install hardware

---
<!-- add words for remove of tape -->
<!-- add added mention for over tighting on heat sink -->
1. Install the CM4 into the Dev Computeblade.
    1. Align the the CM4 with the Computeblade and Apply gentle downward facing pressure to the CM4 - you will hear the connectors snapping in.
    2. Optionally you can also add a Heatsink
2. Install the SSD
    1. Adjust the M.2 standoff the the correct position for your SSD
    2. Remove the Philips screw and and red washer
    3. Insert the edge connector of the SSD at a 45 deg angle in to the M.2 M key connector
    4. Reinstall the retention screw with the red washer

## Prepare CM4 for NVMe Boot

---

To Make sure that the CM4 can boot from the NVMe SSD we will need to update the bootloader. This is done using the `rpiboot` Utility from the USBboot GitHub repo. Once installed

1. navigate to the directory where the executable `rpiboot` is located.
2. Copy the the directory `./recovery`  to a new directory `./nvme` 
3. Edit the copied config file `./nvme/boot.conf` in a text editor and update the `BOOT_ORDER`. Save and close the file 

```tsx
# Try NVMe PCIe, then network
BOOT_ORDER=0xf6
```

:::tip
🌐 To see all boot order configurations see Raspberry Pi [documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#BOOT_ORDER)

:::

1. On the Computeblade make user the USB is Switch to USB-C(Left Position) 
2. Run `./rpiboot -d nvme` 
3. While pressing down the Button labeled `nRPIBOOT`  underneath the USB switch. Connect the the USB-C port to your computer.
4. wait for the command to finish then unplug the USB-C cable

## Frist Connect to Computeblade

---

1. Install SSH Client ([Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui))
2. Connect Computeblade to Power and Network
3. Wait a moment for the blade to boot
4. Enter SSH command to connect to the blade

```bash
SSH <HOSTNAME> -l <USERNAME> 
```

1. Then enter your password

Congratulation your blade is now ready to use. 
We recommend that you update all packages and install our https://github.com/Uptime-Lab/computeblade-agent 

```bash
sudo apt update
sudo apt upgrade
curl -L -o /tmp/computeblade-agent-installer.sh https://raw.githubusercontent.com/Uptime-Lab/computeblade-agent/main/hack/autoinstall.sh
chmod +x /tmp/computeblade-agent-installer.sh
/tmp/computeblade-agent-installer.sh
```

<!-- add trouble shooting section -->