---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #idea
Tags:: [[bootloader]], [[security]], [[linux]]

# rodsboots

# EFI high level principles
- /boot/efi where EFI System Partition (ESP) is normally mounted
- boot loader vs boot manager

# Installation
- Obtain bootloader binary
	- Either through package manager, binary blob, compiled from source
- Copy to /boot/efi folder
- Register bootloader with firmware
	- rEFIt and rEFInd can be run from bootable CDs, avoid need to install on hard disk
	- Or install any EFI bootloader on USB flash drive, treat it like a hard disk
- /boot/efi is the most common mount point for ESP
	- but /boot is also used when using some other bootloaders.
	- Using /boot will complicate kernel update via package managers especially one that use Debian
- New bootloader folder under /boot/efi/EFI/newloader, copy bootloader program's _.efi_ files
- Some bootloader provide installation scripts, typically copy the files and registers bootloader
	- Grub2: grub-install
	- rEFInd: refind-install
- If system already booting using EFI, then efibootmgr can be used to register new bootloader
	- # efibootmgr -c -d /dev/sda -p 1 -l \\EFI\\newloader\\loadername.efi -L NewLoader
	- Note: bootloader path is from ESP's root directory. Using windows style backslash
	- Note: At least one manufacturer shipped products that refuse to boot with very specific bootloader name
- EFI bugs can prevent add boot options when using efibootmgr
	- MacOs _bless_ utility work for HFS+ volume
	- Windows _bcdedit_ can be used to set desired bootloader
	- Windows 3rd party tool EasyUEFI, GUI tool
	- Version 2 of EFI shell, can use _bcfg_ command to register the bootloader
		- # bcfg boot add 3 fs0:\EFI\newloader\loadername.efi "NewLoader"
		- 3: bootnumber
		- fs0:.... path to bootloader
		- Name in EFI boot menu
		- Note: EFI version 2 shell fails with EFIs earlier than 2.31

# Using Grub2
- Most popular, and most complex, but try to do too much, opportunities for misconfiguration and errors.
- Text mode shell for troubleshooting
- Duplicate some functionality provided by EFI or OS-Specific bootloaders
- Manual configuration is usually finicky for EFI system, but setup and configuration scripts are usually good
- 3 method to installing Grub2
	- EFI binary installed on ESP along with support modules and configuration files (Typical of manual setup and Fedora)
	- EFI binary installed on ESP alone, where access additional support and configuration files on Linux root (/)
	- EFI binary read configuration file on ESP, then read secondary configuration file on linux root (/) (Typical of secure boot active on top of the second option)
- grub-install script greatly simplify grub install, and work on most systems
- Add custom entries to /etc/grub.d/40_custom for configuration files to be generated
- _grub-mkconfig -o /boot/grub/grub.cfg_ command to update grub configurations

# CSM: The good, the bad, and the ugly
- EFI is not BIOS, it is fundamentally new type of firmware.
- CSM add-on EFI feature. EFI is always the default/native feature, CSM is optionally enabled.
- CSM does not guarantee a BIOS-mode boot
## The Good
- Old OSes has a conventional BIOS similar to IBM's original IBM PC line
- Without CSM modern EFI based computer can't use old OSes, unless OS add EFI support
- Only very old linux version does not support EFI-based boot, so BIOS compatibility isn't needed for linux-only computer
- CSM interfaces with firmware on plug-in cards, like video cards.
- BIOS boots of modern OSes switch bit depth from 16-bit to 32 or 64-bit depth of the OS. EFI work in CPU's native bit depth. This can cause issue if loading 32 bit OS to 64-bit EFI. CSM allow installation of OS with bit depth differ from EFI.
## The Bad and the Ugly
- EFI's process to determine valid loader is complicated and involves checking multiple locations, and the loader running.
- With CSM the boot process become more complex and harder to reproduce between different machine/setups
## The counter-argument
- Install linux with CSM is with merit since EFI mode installation is not pefect:
	- Incorrectly created boot media: when EFI bootloader is omitted
	- Secure boot problem: may need to enable CSM to allow non-secureboot, or use PreLoader into the boot process to use secureboot
	- Video and other driver problems: should not be an issue more of time, but if do should be able to workaround by disabling grub options
## Manage CSM
	- Linux with systemd, use _systemctl reboot --firmware-setup_
  
---
# References
Rodsboots.com: http://www.rodsbooks.com/efi-bootloaders/index.html
Archlinux wiki page: https://wiki.archlinux.org/index.php/Unified_Extensible_Firmware_Interface
