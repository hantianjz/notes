---
publish: true
review-frequency: normal
---
Last Updated: 2022-12-04
Type:: #documentation 
Tags:: [[Ubuntu]], [[linux]]

# Ubuntu remove old kernel from boot dir

Using Apt
You can remove old kernels with a simple autoremove command in a terminal:

sudo apt-get autoremove --purge
Note: In Ubuntu 14.04, because of Bug #1439769 this works only, if you have installed security updates automatically, and not manually by e.g. Software Updater, see in this section on how to configure it.


The packages to remove are determined based in part on whether the package is marked as manually or automatically installed. You can check if a kernel providing package is marked as automatically installed using this command in a terminal:

```bash
$ apt-mark showauto 'linux-image-.*'
```
or to see if it is marked as manually installed:

```bash
$ apt-mark showmanual 'linux-image-.*'
```
In the event some kernel providing packages are marked as manual (possibly because they were installed via 'apt-get') and you want them autoremoved, you can change the status of the package using apt-mark auto and the package name. For example, to mark kernel 4.12.0-12-generic as autoremovable:


```bash
sudo apt-mark auto '^linux-.*-4\.12\.0-12(-generic)?$'
```
Note: apt-get autoremove will not remove all automatically installed old kernel providing packages as fallback versions are kept; the list of kept kernels is maintained and automatically updated in the file */etc/apt/apt.conf.d/01autoremove-kernels* as a list of matching regular expressions.

Other Methods
If you want to purge one specific kernel providing package you can do so via the following command in a terminal:

```bash
sudo apt-get purge linux-image-4.12.0-12-generic
sudo dpkg --purge linux-headers-4.12.0-12 linux-headers-4.12.0-12-generic
```
This will also purge the corresponding linux-image-extra package if it is installed e.g. linux-image-extra-4.12.0-12-generic. It will not purge linux-headers-4.12.0-12, if there is another linux-headers-4.12.0-12 flavor installed besides -generic.

If you just need to purge kernels selectively, you may benefit from this answer with unofficial code, if the system is not already broken.

There is an unofficial script for purging kernels; it is called linux-purge. By it you can purge kernels selectively, or choose to keep given number of older kernels and remove other depending on options given. It can do do even some fixing (with --fix option), if system is already broken; that is a kind of scripted version of what is told in chapter Safely Removing Old Kernels.

---
# References
- [Remove old kernels](https://help.ubuntu.com/community/RemoveOldKernels)