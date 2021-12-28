#ubuntu

# View currently cached system libs
```bash
$ ldconfig --print-cache
```

# Update LD_LIBRARY_PATH
Add .conf file to `/etc/ld.so.conf.d/` like 

- */etc/ld.so.conf.d/libc*
```
# Some comments
/usr/lib
```

# Refresh library cache
```bash
$ sudo ldconfig
```