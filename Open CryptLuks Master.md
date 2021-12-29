Lasted Updated: 2021-12-29-We
Type: #documentation 
Tags: [[Linux]], [[security]], [[Linux]], [[HOWTO]], [[File Systems]]

# Open CryptLuks Master

```bash
~ ❯❯❯ sudo cryptsetup luksOpen /dev/sda1 secret                    
Enter passphrase for /dev/sda1: 
~ ❯❯❯ sudo mount /dev/mapper/secret /mnt/
~ ❯❯❯ export GNUPGHOME=./master_private
~ ❯❯❯ sudo cryptosetup close secret
~ ❯❯❯ sudo umount /mnt
```

---
# References