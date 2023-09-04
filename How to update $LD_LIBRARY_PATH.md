---
publish: true
review-frequency: normal
link:
- '[[Ubuntu]]'
- '[[Linux]]'
tags:
- documentation
---

# How to update $LD_LIBRARY_PATH

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

Yes, it is normal that you don't have any explicit `LD_LIBRARY_PATH`. Read also [ldconfig(8)](http://man7.org/linux/man-pages/man8/ldconfig.8.html) and [ld-linux(8)](http://man7.org/linux/man-pages/man8/ld-linux.8.html) and about the [rpath](https://en.wikipedia.org/wiki/Rpath). Notice that `ldconfig` updates `/etc/ld.so.cache`, not the `LD_LIBRARY_PATH`. Sometimes you'll set the _rpath_ of an executable explicitly with `-Wl,-rpath,`_directory_ passed to `gcc` at link time.

If you need a `LD_LIBRARY_PATH` (but you probably should not), set it yourself (e.g. in `~/.bashrc`).

If you need system wide settings, you could e.g. consider adding `/usr/local/lib/` in `/etc/ld.so.conf` and run `ldconfig` after installation of every library there.

AFAIK `$LD_LIBRARY_PATH` is used only by the dynamic linker `ld-linux.so` (and by [dlopen(3)](http://man7.org/linux/man-pages/man3/dlopen.3.html) which uses it) after [execve(2)](http://man7.org/linux/man-pages/man2/execve.2.html). See also [ldd(1)](http://man7.org/linux/man-pages/man1/ldd.1.html).