---
publish: true
review-frequency: normal
link:
- '[[rpi]]'
- '[[HOWTO]]'
- '[[Ubuntu]]'
tags:
- documentation
---

# Raspberry Pi - Setup rpi ubuntu

1.  Update password, forced by system
    
2.  Add ssh pub key
    
3.  rename default user from ubuntu to `<new login>`
```bash
$ usermod --login new_username --move-home --home path_to_the_new_home_dir old_username
```
   -   Maybe use root
```bash
$ sudo passwd root
# just go to /etc/ssh/sshd_config change the line as below
PermitRootLogin yes #(i just added this to the bottom of the file)
```
   -   Update sudoless file in /etc/sudoer.d/90-cloud-init-users
	
4. Rename host device