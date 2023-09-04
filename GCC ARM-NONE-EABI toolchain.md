---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #documentation 
Tags:: [[embedded]], [[arm]], [[gcc]], [[toolchain]]

# GCC ARM-NONE-EABI toolchain

Current latest version **10.3-2021.10** https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads

# [How to install with deps](https://askubuntu.com/questions/1243252/how-to-install-arm-none-eabi-gdb-on-ubuntu-20-04-lts-focal-fossa)

Download latest version (Linux x86_64 Tarball) from their website, check its MD5. Unpack it into some directory. I used /usr/share/ :

`sudo tar xjf gcc-arm-none-eabi-your-version.bz2 -C /usr/share/`

Create links so that binaries are accessible system-wide:
```
sudo ln -s /usr/share/gcc-arm-none-eabi-your-version/bin/arm-none-eabi-gcc /usr/bin/arm-none-eabi-gcc 
sudo ln -s /usr/share/gcc-arm-none-eabi-your-version/bin/arm-none-eabi-g++ /usr/bin/arm-none-eabi-g++
sudo ln -s /usr/share/gcc-arm-none-eabi-your-version/bin/arm-none-eabi-gdb /usr/bin/arm-none-eabi-gdb
sudo ln -s /usr/share/gcc-arm-none-eabi-your-version/bin/arm-none-eabi-size /usr/bin/arm-none-eabi-size
```

Install dependencies. ARM's "full installation instructions" listed in readme.txt won't tell you what dependencies are - you have to figure it out by trial and error. In my system I had to manually create symbolic links to force it to work:

```
sudo apt install libncurses-dev
sudo ln -s /usr/lib/x86_64-linux-gnu/libncurses.so.6 /usr/lib/x86_64-linux-gnu/libncurses.so.5
sudo ln -s /usr/lib/x86_64-linux-gnu/libtinfo.so.6 /usr/lib/x86_64-linux-gnu/libtinfo.so.5
```

Check if it works:
```
arm-none-eabi-gcc --version
arm-none-eabi-g++ --version
arm-none-eabi-gdb --version
arm-none-eabi-size --version
```

# Ubuntu Install
```
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo apt install gcc-multilib
```

---
# References
- https://embeddedinventor.com/a-complete-beginners-guide-to-the-gnu-arm-toolchain-part-1/