---
publish: true
review-frequency: ignore
link:
- '[[Linux]]'
- '[[security]]'
- '[[Linux]]'
- '[[HOWTO]]'
- '[[File Systems]]'
- '[[password-store]]'
- '[[gpg]]'
tags:
- documentation
---
# Open CryptLuks Master

```bash
sudo cryptsetup luksOpen /dev/sda1 secret                    
sudo mount /dev/mapper/secret /mnt/
cd /mnt
export GNUPGHOME=./master_private
# do you things
sudo umount /mnt
sudo cryptsetup luksClose secret
```