---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #idea
Tags:: [[arm]], [[linux]], [[qemu]], [[simulation]], [[rpi]]

# QEMU

# Linux files
zImage: Compressed linux kernel file
rootfs/initramfs: Minimal file system images with kernel modules, init procedure scripts, and neccessary binaries to boot a full system.
dtb: device tree to describe underlaying hardware and achieve portability (More reading)

# Build plan
+ Build the kernel first outside of buildroot
+ Run with minimal rootfs in qemu
+ Reproduce the same build result with buildroot, ensure changes to the kernel is actually refected
- Modify kernel build for rpi3, and load same build on HW

# Building notes:
Using the rpi linux kernel fork git@github.com:raspberrypi/linux.git
Checked out tag tags/raspberrypi-kernel_1.20180619-1, this looks like it is the most recent release version

qemu-system-aarch64 seem to already support raspi3. Will attempt to build that and if we can boot the default image.
So the default build does work....none of the work was needed...

---
# References
https://medicineyeh.wordpress.com/2016/03/29/buildup-your-arm-image-for-qemu/