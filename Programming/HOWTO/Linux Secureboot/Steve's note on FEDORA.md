---
publish: true
review-frequency: normal
---
Last Updated: 2021-12-29
Type:: #documentation 
Tags:: [[bootloader]], [[security]], [[linux]]

# Steve's note on FEDORA

# FC26

Okay, here we go. these are the condensed install steps for getting an
encrypted boot on fedora. There are some guides out there that are
somewhat helpful, but not complete, most notably:
https://dustymabe.com/2015/07/06/encrypting-more-boot-joins-the-party/

This can all be done with secure boot enabled!

- boot into live cd, open terminal
- assume no partitions are created:

1. fdisk create partition 5 and 6, 5 large, 6 small for boot
   use type 31 for LVM on type 5
3. cryptsetup luksFormat --hash=sha512 --cipher=aes-xts-plain64 --key-size=512 /dev/nvme0n1p5
4. cryptsetup luksOpen /dev/nvme0n1p5 luks
5. pvcreate /dev/mapper/luks
6. vgcreate vg0 /dev/mapper/luks
7. lvcreate -L 32G -n swap vg0
8. lvcreate -L 32G -n root vg0
9. lvcreate -L 64G -n home vg0
10. Install fedora normally

- boog in fedora installer that root must be formatted, whatever.
- boog doesn't let me use /dev/sda in installer for USB.

- after install:

1. umount -R /mnt/sysimage/boot
2. mkdir -p /mnt/boot
3. mount /dev/nvme0n1p6 /mnt/boot
4. cp -a /mnt/boot/. /mnt/sysimage/boot
5. edit /mnt/sysimage/etc/fstab to remove /boot line

- okay, let's try unmounting everything:

1. umount -R /mnt/sysimage /mnt/boot
2. swapoff /dev/mapper/vg0-swap
2. vgchange -an vg0
2. cryptsetup luksClose luks

- alternatively, can be done on an installed system by rebooting to live cd
- if this works, then we can fix the partitions. nuke p6 and make p5
  larger. resize the pv for lost space. otherwise reboot. might need
  partprobe.

1. cryptsetup luksOpen /dev/nvme0n1p5 luks
2. pvresize /dev/mapper/luks

- okay, now we can remount everything and get to work

1. mount /dev/mapper/vg0-root /mnt/sysimage
2. mount /dev/mapper/vg0-home /mnt/sysimage/home
3. mount /dev/nvme0n1p1 /mnt/sysimage/boot/efi
4. mount --bind /dev /mnt/sysimage/dev
5. mount --bind /proc /mnt/sysimage/proc
6. mount --bind /sys /mnt/sysimage/sys
6. mount --bind /sys/firmware/efi/efivars /mnt/sysimage/sys/firmware/efi/efivars
7. chroot /mnt/sysimage

- lets hack some things up, first generate keyfile
- the following sections can be done on a live system

1. dd if=/dev/urandom of=/crypto_keyfile.bin bs=4k count=1
2. chmod 000 /crypto_keyfile.bin
3. cryptosetup luksAddKey /dev/nvme0n1p5 /crypto_keyfile.bin
4. edit /etc/crypttab to replace 'none' with: /crypto_keyfile.bin luks
5. edit /etc/dracut.conf.d/10-crypto_keyfile.conf with contents:
    install_items+="/crypto_keyfile.bin"
6. generate initramfs: dracut -f

- finally, lets fix up grub

> 1. dnf install grub2-efi-modules
> 2. cp -a /usr/lib/grub/x86_64-efi /boot/efi/EFI/fedora
> 3. add GRUB_ENABLE_CRYPTODISK=y to /etc/default/grub
> 4. grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg

But wait, surely we can do better!

```bash
# dnf -y install grub2-efi-modules
```

we should only need to lock: grub2-efi and grub2-efi-modules

```bash
# dnf -y install "dnf-command(versionlock)"
# dnf versionlock grub2-efi grub2-efi-modules
```

look at crypto.lst to know which algo's to grab: aes -> gcry_rijndael, gcry_sha512

```bash
# grub2-mkimage -O x86_64-efi -p /boot/efi/EFI/fedora -o grubx64.efi all_video boot btrfs cat chain configfile echo efifwsetup efinet ext2 fat font gfxmenu gfxterm gzio halt hfsplus iso9660 jpeg loadenv loopback lvm mdraid09 mdraid1x minicmd normal part_apple part_msdos part_gpt password_pbkdf2 png reboot search search_fs_uuid search_fs_file search_label serial sleep syslinuxcfg test tftp video xfs crypto cryptodisk luks gcry_rijndael gcry_sha512
```

should create a makefile for this...

```bash
# dnf install pesign
```

generate certificate and sign grub binary:

```bash
# efikeygen -S -d /etc/pki/pesign -n precision -c "CN=precision.mission-bay.net, CN=Secure Boot Certificate" -k

# pesign -i grubx64.efi -o grubx64.efi-signed -n /etc/pki/pesign -c precision -s
```

(heed warning from: https://fedoraproject.org/wiki/User:Pjones/SecureBootSelfSigning)

```bash
# certutil -L -d /etc/pki/pesign -n precision -o cert.der -r
# mokutil -i cert.der

# cp -f grubx64.efi-signed /boot/efi/EFI/fedora/grubx64.efi
```

makefile:

```bash
# curl <gist URL> | make -f - enroll install

--> curl -L https://git.io/vdKIp | make -f - enroll install
```

to show key to be enrolled

```bash
# mokutil --list-new
```

finally:

1. add GRUB_ENABLE_CRYPTODISK=y to /etc/default/grub
2. grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg

- That should be it - reboot and hope.

1. exit chroot
2. reboot & enroll MOK

- to reverse custom grub stuff:

```bash
# dnf versionlock delete grub-efi grub-efi-modules
# dnf reinstall grub-efi
```

# FEDORA LOG
```bash
[liveuser@localhost-live ~]$ sudo -i
[root@localhost-live ~]# fdisk /dev/nvme0n1

Welcome to fdisk (util-linux 2.29.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk /dev/nvme0n1: 477 GiB, 512110190592 bytes, 1000215216 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: C051E360-8899-46B8-89A7-104F94636121

Device             Start       End   Sectors   Size Type
/dev/nvme0n1p1      2048   1126399   1124352   549M EFI System
/dev/nvme0n1p2   1126400   1159167     32768    16M Microsoft reserved
/dev/nvme0n1p3   1159168 498359710 497200543 237.1G Microsoft basic data
/dev/nvme0n1p4 498360320 500119551   1759232   859M Windows recovery environment

Command (m for help): n
Partition number (5-128, default 5): 
First sector (500119552-1000215182, default 500119552): 
Last sector, +sectors or +size{K,M,G,T,P} (500119552-1000215182, default 1000215182): +237G

Created a new partition 5 of type 'Linux filesystem' and of size 237 GiB.

Command (m for help): t
Partition number (1-5, default 5): 5
Hex code (type L to list all codes): 31

Changed type of partition 'Linux filesystem' to 'Linux LVM'.

Command (m for help): n
Partition number (6-128, default 6): 
First sector (997144576-1000215182, default 997144576): 
Last sector, +sectors or +size{K,M,G,T,P} (997144576-1000215182, default 1000215182): 

Created a new partition 6 of type 'Linux filesystem' and of size 1.5 GiB.

Command (m for help): p
Disk /dev/nvme0n1: 477 GiB, 512110190592 bytes, 1000215216 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: C051E360-8899-46B8-89A7-104F94636121

Device             Start        End   Sectors   Size Type
/dev/nvme0n1p1      2048    1126399   1124352   549M EFI System
/dev/nvme0n1p2   1126400    1159167     32768    16M Microsoft reserved
/dev/nvme0n1p3   1159168  498359710 497200543 237.1G Microsoft basic data
/dev/nvme0n1p4 498360320  500119551   1759232   859M Windows recovery environment
/dev/nvme0n1p5 500119552  997144575 497025024   237G Linux LVM
/dev/nvme0n1p6 997144576 1000215182   3070607   1.5G Linux filesystem

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

[root@localhost-live ~]# cryptsetup luksFormat --hash=sha512 --cipher=aes-xts-plain64 --key-size=512 /dev/nvme0n1p5

WARNING!
========
This will overwrite data on /dev/nvme0n1p5 irrevocably.

Are you sure? (Type uppercase yes): YES
Enter passphrase: 
Verify passphrase: 
[root@localhost-live ~]# cryptsetup luksOpen /dev/nvme0n1p5 luks
Enter passphrase for /dev/nvme0n1p5: 
[root@localhost-live ~]# pvcreate /dev/mapper/luks 
  Physical volume "/dev/mapper/luks" successfully created.
[root@localhost-live ~]# vgcreate vg0 /dev/mapper/luks 
  Volume group "vg0" successfully created
[root@localhost-live ~]# lvcreate -L 32G -n swap vg0
  Logical volume "swap" created.
[root@localhost-live ~]# lvcreate -L 32G -n root vg0
  Logical volume "root" created.
[root@localhost-live ~]# lvcreate -L 64G -n home vg0
  Logical volume "home" created.
[root@localhost-live ~]# 
[root@localhost-live ~]# # install fedora
[root@localhost-live ~]# 
[root@localhost-live ~]# umount -R /mnt/sysimage/boot
[root@localhost-live ~]# mkdir -p /mnt/boot
[root@localhost-live ~]# mount /dev/nvme0n1p6 /mnt/boot
[root@localhost-live ~]# cp -a /mnt/boot/. /mnt/sysimage/boot
[root@localhost-live ~]# vi /mnt/sysimage/etc/fstab ^C
[root@localhost-live ~]# ^C
[root@localhost-live ~]# sudo -i -e '#/dev/nvme0n1p6#d' /mnt/sysimage/etc/fstab 
usage: sudo -h | -K | -k | -V
usage: sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]
usage: sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]
usage: sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T
            timeout] [-u user] [VAR=value] [-i|-s] [<command>]
usage: sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T
            timeout] [-u user] file ...
[root@localhost-live ~]# sed -i -e '#/dev/nvme0n1p6#d' /mnt/sysimage/etc/fstab 
[root@localhost-live ~]# 
[root@localhost-live ~]# # dumb. just edit.
[root@localhost-live ~]# vi /mnt/sysimage/etc/fstab 
[root@localhost-live ~]# 
[root@localhost-live ~]# umount -R /mnt/sysimage /mnt/boot 
[root@localhost-live ~]# swapoff /dev/mapper/vg0-swap
[root@localhost-live ~]# vgchange -an vg0
  0 logical volume(s) in volume group "vg0" now active
[root@localhost-live ~]# cryptsetup luksClose luks
[root@localhost-live ~]# 
[root@localhost-live ~]# # resize partitions
[root@localhost-live ~]# 
[root@localhost-live ~]# fdisk /dev/nvme0n1

Welcome to fdisk (util-linux 2.29.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk /dev/nvme0n1: 477 GiB, 512110190592 bytes, 1000215216 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: C051E360-8899-46B8-89A7-104F94636121

Device             Start        End   Sectors   Size Type
/dev/nvme0n1p1      2048    1126399   1124352   549M EFI System
/dev/nvme0n1p2   1126400    1159167     32768    16M Microsoft reserved
/dev/nvme0n1p3   1159168  498359710 497200543 237.1G Microsoft basic data
/dev/nvme0n1p4 498360320  500119551   1759232   859M Windows recovery environment
/dev/nvme0n1p5 500119552  997144575 497025024   237G Linux LVM
/dev/nvme0n1p6 997144576 1000215182   3070607   1.5G Linux filesystem

Command (m for help): d
Partition number (1-6, default 6): 6

Partition 6 has been deleted.

Command (m for help): d
Partition number (1-5, default 5): 5

Partition 5 has been deleted.

Command (m for help): n
Partition number (5-128, default 5): 
First sector (500119552-1000215182, default 500119552): 
Last sector, +sectors or +size{K,M,G,T,P} (500119552-1000215182, default 1000215182): 

Created a new partition 5 of type 'Linux filesystem' and of size 238.5 GiB.
Partition #5 contains a crypto_LUKS signature.

Do you want to remove the signature? [Y]es/[N]o: n

Command (m for help): p

Disk /dev/nvme0n1: 477 GiB, 512110190592 bytes, 1000215216 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: C051E360-8899-46B8-89A7-104F94636121

Device             Start        End   Sectors   Size Type
/dev/nvme0n1p1      2048    1126399   1124352   549M EFI System
/dev/nvme0n1p2   1126400    1159167     32768    16M Microsoft reserved
/dev/nvme0n1p3   1159168  498359710 497200543 237.1G Microsoft basic data
/dev/nvme0n1p4 498360320  500119551   1759232   859M Windows recovery environment
/dev/nvme0n1p5 500119552 1000215182 500095631 238.5G Linux filesystem

Command (m for help): t
Partition number (1-5, default 5): 5
Hex code (type L to list all codes): 31

Changed type of partition 'Linux filesystem' to 'Linux LVM'.

Command (m for help): p
Disk /dev/nvme0n1: 477 GiB, 512110190592 bytes, 1000215216 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: C051E360-8899-46B8-89A7-104F94636121

Device             Start        End   Sectors   Size Type
/dev/nvme0n1p1      2048    1126399   1124352   549M EFI System
/dev/nvme0n1p2   1126400    1159167     32768    16M Microsoft reserved
/dev/nvme0n1p3   1159168  498359710 497200543 237.1G Microsoft basic data
/dev/nvme0n1p4 498360320  500119551   1759232   859M Windows recovery environment
/dev/nvme0n1p5 500119552 1000215182 500095631 238.5G Linux LVM

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

[root@localhost-live ~]# 
[root@localhost-live ~]# 
[root@localhost-live ~]# cryptsetup luksOpen /dev/nvme0n1p5 luks
Enter passphrase for /dev/nvme0n1p5: 
[root@localhost-live ~]# pvresize /dev/mapper/luks 
  Physical volume "/dev/mapper/luks" changed
  1 physical volume(s) resized / 0 physical volume(s) not resized
[root@localhost-live ~]# pvs
  PV               VG  Fmt  Attr PSize   PFree  
  /dev/mapper/luks vg0 lvm2 a--  238.46g 110.46g
[root@localhost-live ~]# 
[root@localhost-live ~]# 
[root@localhost-live ~]# mount /dev/mapper/vg0-root /mnt/sysimage/
[root@localhost-live ~]# mount /dev/mapper/vg0-home /mnt/sysimage/home/
[root@localhost-live ~]# mount /dev/nvme0n1p
nvme0n1p1  nvme0n1p2  nvme0n1p3  nvme0n1p4  nvme0n1p5  
[root@localhost-live ~]# mount /dev/nvme0n1p1 /mnt/sysimage/boot/efi/
[root@localhost-live ~]# mount --bind /dev /mnt/sysimage/dev/
[root@localhost-live ~]# mount --bind /proc /mnt/sysimage/proc/
[root@localhost-live ~]# mount --bind /sys /mnt/sysimage/sys/
[root@localhost-live ~]# chroot /mnt/sysimage/
[root@precision /]# 
[root@precision /]# 
[root@precision /]# dd if=/dev/urandom of=/crypto_keyfile.bin bs=4K count=1
1+0 records in
1+0 records out
4096 bytes (4.1 kB, 4.0 KiB) copied, 0.00028595 s, 14.3 MB/s
[root@precision /]# dd if=/dev/urandom of=/crypto_keyfile.bin bs=4k count=1
1+0 records in
1+0 records out
4096 bytes (4.1 kB, 4.0 KiB) copied, 0.00688119 s, 595 kB/s
[root@precision /]# chmod 000 /crypto_keyfile.bin 
[root@precision /]# cryptsetup luksAddKey /dev/nvme0n1p5 /crypto_keyfile.bin 
Enter any existing passphrase: 
[root@precision /]# vi /etc/crypttab 
[root@precision /]# echo 'install_items+="/crypto_keyfile.bin"' > /etc/dracut.conf.d/10-crypto_keyfile.conf
[root@precision /]# dracut -f
dracut: No '/dev/log' or 'logger' included for syslog logging
[root@precision /]# 
[root@precision /]# 
[root@precision /]# dnf install grub2-efi-modules
Fedora 26 - x86_64 - Updates                                  2.5 MB/s |  15 MB     00:06    
Fedora 26 - x86_64                                            3.8 MB/s |  53 MB     00:14    
Last metadata expiration check: 0:00:07 ago on Tue 10 Oct 2017 07:36:55 PM CDT.
Dependencies resolved.
==============================================================================================
 Package                    Arch            Version                     Repository       Size
==============================================================================================
Installing:
 grub2-efi-modules          x86_64          1:2.02-0.40.fc26            fedora          3.6 M

Transaction Summary
==============================================================================================
Install  1 Package

Total download size: 3.6 M
Installed size: 20 M
Is this ok [y/N]: y
Downloading Packages:
grub2-efi-modules-2.02-0.40.fc26.x86_64.rpm                   3.0 MB/s | 3.6 MB     00:01    
----------------------------------------------------------------------------------------------
Total                                                         2.3 MB/s | 3.6 MB     00:01     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                      1/1 
  Installing       : grub2-efi-modules-1:2.02-0.40.fc26.x86_64                            1/1 
  Verifying        : grub2-efi-modules-1:2.02-0.40.fc26.x86_64                            1/1 

Installed:
  grub2-efi-modules.x86_64 1:2.02-0.40.fc26                                                   

Complete!
[root@precision /]# dnf -y install 'dnf-command(versionlock)'
Last metadata expiration check: 0:00:46 ago on Tue 10 Oct 2017 07:36:55 PM CDT.
Dependencies resolved.
==============================================================================================
 Package                              Arch         Version                Repository     Size
==============================================================================================
Installing:
 python3-dnf-plugin-versionlock       noarch       2.1.5-1.fc26           updates        46 k
Upgrading:
 dnf                                  noarch       2.7.3-1.fc26           updates       340 k
 dnf-conf                             noarch       2.7.3-1.fc26           updates        67 k
 dnf-plugins-core                     noarch       2.1.5-1.fc26           updates        50 k
 dnf-yum                              noarch       2.7.3-1.fc26           updates        48 k
 libdnf                               x86_64       0.10.1-1.fc26          updates       126 k
 python3-dnf                          noarch       2.7.3-1.fc26           updates       455 k
 python3-dnf-plugins-core             noarch       2.1.5-1.fc26           updates       141 k
 python3-hawkey                       x86_64       0.10.1-1.fc26          updates        51 k

Transaction Summary
==============================================================================================
Install  1 Package
Upgrade  8 Packages

Total download size: 1.3 M
Downloading Packages:
(1/9): python3-hawkey-0.9.1-1.fc26_0.10.1-1.fc26.x86_64.drpm  119 kB/s |  25 kB     00:00    
(2/9): python3-dnf-plugins-core-2.1.1-1.fc26_2.1.5-1.fc26.noa 186 kB/s |  66 kB     00:00    
[DRPM 1/5] python3-hawkey-0.9.1-1.fc26_0.10.1-1.fc26.x86_64.drpm: done                       
(3/9): libdnf-0.9.1-1.fc26_0.10.1-1.fc26.x86_64.drpm          259 kB/s |  56 kB     00:00    
(4/9): python3-dnf-2.5.1-1.fc26_2.7.3-1.fc26.noarch.drpm      264 kB/s | 129 kB     00:00    
(5/9): python3-dnf-plugin-versionlock-2.1.5-1.fc26.noarch.rpm 329 kB/s |  46 kB     00:00    
(6/9): dnf-conf-2.7.3-1.fc26.noarch.rpm                       459 kB/s |  67 kB     00:00    
(7/9): dnf-2.5.1-1.fc26_2.7.3-1.fc26.noarch.drpm              544 kB/s | 186 kB     00:00    
[DRPM 2/5] python3-dnf-plugins-core-2.1.1-1.fc26_2.1.5-1.fc26.noarch.drpm: done              
[DRPM 3/5] libdnf-0.9.1-1.fc26_0.10.1-1.fc26.x86_64.drpm: done                               
(8/9): dnf-plugins-core-2.1.5-1.fc26.noarch.rpm               365 kB/s |  50 kB     00:00    
(9/9): dnf-yum-2.7.3-1.fc26.noarch.rpm                        629 kB/s |  48 kB     00:00    
[DRPM 4/5] python3-dnf-2.5.1-1.fc26_2.7.3-1.fc26.noarch.drpm: done                           
[DRPM 5/5] dnf-2.5.1-1.fc26_2.7.3-1.fc26.noarch.drpm: done                                   
----------------------------------------------------------------------------------------------
Total                                                         456 kB/s | 673 kB     00:01     
Delta RPMs reduced 1.3 MB of updates to 0.7 MB (49.1% saved)
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Running scriptlet: None                                                                 1/1 
  Preparing        :                                                                      1/1 
  Upgrading        : libdnf-0.10.1-1.fc26.x86_64                                         1/17 
  Running scriptlet: libdnf-0.10.1-1.fc26.x86_64                                         1/17 
  Upgrading        : python3-hawkey-0.10.1-1.fc26.x86_64                                 2/17 
  Upgrading        : dnf-conf-2.7.3-1.fc26.noarch                                        3/17 
  Upgrading        : python3-dnf-2.7.3-1.fc26.noarch                                     4/17 
  Upgrading        : python3-dnf-plugins-core-2.1.5-1.fc26.noarch                        5/17 
  Upgrading        : dnf-2.7.3-1.fc26.noarch                                             6/17 
  Running scriptlet: dnf-2.7.3-1.fc26.noarch                                             6/17 
  Upgrading        : dnf-yum-2.7.3-1.fc26.noarch                                         7/17 
  Installing       : python3-dnf-plugin-versionlock-2.1.5-1.fc26.noarch                  8/17 
  Upgrading        : dnf-plugins-core-2.1.5-1.fc26.noarch                                9/17 
  Cleanup          : dnf-yum-2.5.1-1.fc26.noarch                                        10/17 
  Running scriptlet: dnf-2.5.1-1.fc26.noarch                                            11/17 
  Cleanup          : dnf-2.5.1-1.fc26.noarch                                            11/17 
  Running scriptlet: dnf-2.5.1-1.fc26.noarch                                            11/17 
Running in chroot, ignoring request.
  Cleanup          : dnf-plugins-core-2.1.1-1.fc26.noarch                               12/17 
  Cleanup          : python3-dnf-plugins-core-2.1.1-1.fc26.noarch                       13/17 
  Cleanup          : python3-dnf-2.5.1-1.fc26.noarch                                    14/17 
  Cleanup          : python3-hawkey-0.9.1-1.fc26.x86_64                                 15/17 
  Cleanup          : dnf-conf-2.5.1-1.fc26.noarch                                       16/17 
  Cleanup          : libdnf-0.9.1-1.fc26.x86_64                                         17/17 
  Running scriptlet: libdnf-0.9.1-1.fc26.x86_64                                         17/17 
Running in chroot, ignoring request.
  Verifying        : python3-dnf-plugin-versionlock-2.1.5-1.fc26.noarch                  1/17 
  Verifying        : python3-dnf-plugins-core-2.1.5-1.fc26.noarch                        2/17 
  Verifying        : python3-dnf-2.7.3-1.fc26.noarch                                     3/17 
  Verifying        : dnf-conf-2.7.3-1.fc26.noarch                                        4/17 
  Verifying        : python3-hawkey-0.10.1-1.fc26.x86_64                                 5/17 
  Verifying        : dnf-plugins-core-2.1.5-1.fc26.noarch                                6/17 
  Verifying        : libdnf-0.10.1-1.fc26.x86_64                                         7/17 
  Verifying        : dnf-2.7.3-1.fc26.noarch                                             8/17 
  Verifying        : dnf-yum-2.7.3-1.fc26.noarch                                         9/17 
  Verifying        : dnf-plugins-core-2.1.1-1.fc26.noarch                               10/17 
  Verifying        : dnf-yum-2.5.1-1.fc26.noarch                                        11/17 
  Verifying        : python3-dnf-2.5.1-1.fc26.noarch                                    12/17 
  Verifying        : python3-dnf-plugins-core-2.1.1-1.fc26.noarch                       13/17 
  Verifying        : libdnf-0.9.1-1.fc26.x86_64                                         14/17 
  Verifying        : python3-hawkey-0.9.1-1.fc26.x86_64                                 15/17 
  Verifying        : dnf-2.5.1-1.fc26.noarch                                            16/17 
  Verifying        : dnf-conf-2.5.1-1.fc26.noarch                                       17/17 

Installed:
  python3-dnf-plugin-versionlock.noarch 2.1.5-1.fc26                                          

Upgraded:
  dnf.noarch 2.7.3-1.fc26                            dnf-conf.noarch 2.7.3-1.fc26             
  dnf-plugins-core.noarch 2.1.5-1.fc26               dnf-yum.noarch 2.7.3-1.fc26              
  libdnf.x86_64 0.10.1-1.fc26                        python3-dnf.noarch 2.7.3-1.fc26          
  python3-dnf-plugins-core.noarch 2.1.5-1.fc26       python3-hawkey.x86_64 0.10.1-1.fc26      

Complete!
[root@precision /]# dnf versionlock grub2-efi grub2-efi-modules
Last metadata expiration check: 0:01:11 ago on Tue 10 Oct 2017 07:36:55 PM CDT.
Adding versionlock on: grub2-efi-modules-1:2.02-0.40.fc26.*
Adding versionlock on: grub2-efi-1:2.02-0.40.fc26.*
[root@precision /]# cd
[root@precision ~]# scp stallion@bailiwick:Backup/Makefile .
The authenticity of host 'bailiwick (10.51.0.16)' can't be established.
RSA key fingerprint is SHA256:bR846wP/1s0LwAa7MgwyooVWettNxEYU/Oj+6K3Y9hI.
RSA key fingerprint is MD5:13:08:a5:50:a3:ab:0f:96:06:65:ec:f1:8a:db:6c:63.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'bailiwick,10.51.0.16' (RSA) to the list of known hosts.
stallion@bailiwick's password: 
dPermission denied, please try again.
stallion@bailiwick's password: 
Makefile                                                    100% 2599   325.4KB/s   00:00    
[root@precision ~]# dnf -y install mokutil nss-tools pesign
Last metadata expiration check: 0:02:10 ago on Tue 10 Oct 2017 07:36:55 PM CDT.
Package mokutil-1:0.3.0-4.fc26.x86_64 is already installed, skipping.
Package nss-tools-3.30.2-1.1.fc26.x86_64 is already installed, skipping.
Dependencies resolved.
==============================================================================================
 Package            Arch               Version                      Repository           Size
==============================================================================================
Installing:
 pesign             x86_64             0.112-20.fc26                updates             176 k

Transaction Summary
==============================================================================================
Install  1 Package

Total download size: 176 k
Installed size: 1.0 M
Downloading Packages:
pesign-0.112-20.fc26.x86_64.rpm                               303 kB/s | 176 kB     00:00    
----------------------------------------------------------------------------------------------
Total                                                         167 kB/s | 176 kB     00:01     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                      1/1 
  Running scriptlet: pesign-0.112-20.fc26.x86_64                                          1/1 
  Installing       : pesign-0.112-20.fc26.x86_64                                          1/1 
  Running scriptlet: pesign-0.112-20.fc26.x86_64                                          1/1 
Running in chroot, ignoring request.
  Verifying        : pesign-0.112-20.fc26.x86_64                                          1/1 

Installed:
  pesign.x86_64 0.112-20.fc26                                                                 

Complete!
[root@precision ~]# efikeygen -S -d /etc/pki/pesign -n precision -c "CN=Secure Boot Certificate,CN=precision.mission-bay.net" -k
tag: 362
[root@precision ~]# make enroll
certutil -L -d /etc/pki/pesign -n precision -o /tmp/tmp.QMkdlQwDjR -r
mokutil -i /tmp/tmp.QMkdlQwDjR
input password: 
input password again: 
rm -f /tmp/tmp.QMkdlQwDjR
[root@precision ~]# make install
grub2-mkimage -O x86_64-efi -p /boot/efi/EFI/fedora -o grubx64.efi all_video boot btrfs cat chain configfile echo efifwsetup efinet ext2 fat font gfxmenu gfxterm gzio halt hfsplus iso9660 jpeg loadenv loopback lvm mdraid09 mdraid1x minicmd normal part_apple part_msdos part_gpt password_pbkdf2 png reboot search search_fs_uuid search_fs_file search_label serial sleep syslinuxcfg test tftp video xfs cryptodisk luks gcry_rijndael gcry_sha512
pesign -i grubx64.efi -o grubx64.efi-signed -n /etc/pki/pesign -c precision -s
cp -f -v grubx64.efi-signed /boot/efi/EFI/fedora/grubx64.efi
'grubx64.efi-signed' -> '/boot/efi/EFI/fedora/grubx64.efi'
[root@precision ~]# echo "GRUB_ENABLE_CRYPTODISK=y" >>/etc/default/grub 
[root@precision ~]# grub2-mk
grub2-mkconfig         grub2-mklayout         grub2-mkrelpath        
grub2-mkfont           grub2-mknetdir         grub2-mkrescue         
grub2-mkimage          grub2-mkpasswd-pbkdf2  grub2-mkstandalone     
[root@precision ~]# grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg 
Generating grub configuration file ...
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
Found linux image: /boot/vmlinuz-4.11.8-300.fc26.x86_64
Found initrd image: /boot/initramfs-4.11.8-300.fc26.x86_64.img
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
Found linux image: /boot/vmlinuz-0-rescue-7e5cdac97db74b52823982cb37577c3b
Found initrd image: /boot/initramfs-0-rescue-7e5cdac97db74b52823982cb37577c3b.img
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
  WARNING: Failed to connect to lvmetad. Falling back to device scanning.
device-mapper: reload ioctl on osprober-linux-sda1 failed: Device or resource busy
Command failed
done
[root@precision ~]#
```
# Makefile
```makefile
# Copyright (c) 2017 Steven Stallion
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

CERT_DIR	?= /etc/pki/pesign
CERT_NICKNAME	?= $(shell hostname)
GRUB_FORMAT	?= x86_64-efi
GRUB_IMAGE	?= grubx64.efi
GRUB_PREFIX	?= /boot/efi/EFI/fedora

# The default list of modules included by grub2.spec;
# see: http://pkgs.fedoraproject.org/cgit/rpms/grub2.git/tree/grub2.spec
define GRUB_MODULES
all_video boot btrfs cat chain configfile echo efifwsetup efinet ext2 \
fat font gfxmenu gfxterm gzio halt hfsplus iso9660 jpeg loadenv \
loopback lvm mdraid09 mdraid1x minicmd normal part_apple part_msdos \
part_gpt password_pbkdf2 png reboot search search_fs_uuid \
search_fs_file search_label serial sleep syslinuxcfg test tftp video \
xfs
endef

define GRUB_EXTRA_MODULES
cryptodisk luks gcry_rijndael gcry_sha512 gfxterm_background gfxterm_menu
endef

.PHONY:	all clean enroll install

all:	$(GRUB_IMAGE) $(GRUB_IMAGE)-signed

clean:
	rm -f $(GRUB_IMAGE) $(GRUB_IMAGE)-signed

enroll:
	$(eval TMP = $(shell mktemp))
	certutil -L -d $(CERT_DIR) -n $(CERT_NICKNAME) -o $(TMP) -r
	mokutil -i $(TMP)
	rm -f $(TMP)

install: $(GRUB_IMAGE)-signed
	cp -f -v $< $(GRUB_PREFIX)/$(GRUB_IMAGE)

$(GRUB_IMAGE):
	grub2-mkimage -O $(GRUB_FORMAT) -p $(GRUB_PREFIX) -o $@ $(GRUB_MODULES) $(GRUB_EXTRA_MODULES)

$(GRUB_IMAGE)-signed: $(GRUB_IMAGE)
	pesign -i $< -o $@ -n $(CERT_DIR) -c $(CERT_NICKNAME) -s
```