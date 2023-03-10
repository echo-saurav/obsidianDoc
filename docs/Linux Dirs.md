---
layout: default
title: Linux Dirs
---
# Linux Dirs
- [ ] convert this to excalidraw drawing #todo 

# Linux Dir structure . for more info [Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) #linux
- **/home/username/**
   - **/home/username/.local** its same as root */usr/* but user specific file
      - **/home/username/.local/share** user data folder
      - **/home/username/.local/include**
      - **/home/username/.local/lib**
      - **/home/username/.local/bin**
   - **/home/username/.config** config files for program (more like etc but user specific)
   - **/home/username/.cache** non-essential data files , unlike **share** these folder can be deleted
- **/opt** all installed software and there's binaries
- **/tmp** things here will be deleted when reboot
- **/var** contains variable data files. This includes spool directories and files, administrative and logging data, and transient and temporary files
   - **/var/spool** data which is awaiting some kind of later processing. Often data is deleted after it has been processed
      - **/cron/crontab** [[Database/Cron Job]] script for program to run in an time interval ⏰
   - **/var/run** symbolic link to */run*
   - **/var/log** This directory contains miscellaneous log files. Most logs must be written to this directory or an appropriate subdirectory
- **/etc** program config files folder
   - **fstab** mounting point
   - **passwd** store passwords in hash
- **/dev** Contains device files for all hardware devices
   - **/dev/null** move things here that dont needed
   - **/dev/random** kernel RNG from hardware
- not actual device but generated **/proc**
- **/bin** contains executables which are required by the system for emergency repairs, booting, and single user mode
- **/sbin** Binaries needed for booting, low-level system repair, or maintenance (run level 1 or S)
- **/usr**
   - **/usr/bin** Application/distribution binaries meant to be accessed by locally logged in users * (there are many binaries smlinked from
   - **/share** Any program or package which contains or requires data that doesn't need to be modified should store that data here
      - **/usr/share/dict**
         - files with word in many language
      - **/usr/share/zoneinfo** Timezone information and configuration
   - **/usr/include** This is where all of the system's general-use include files for the C programming language should be placed
   - **/usr/lib** includes object files and libraries. [21] On some systems, it may also include internal binaries that are not intended to be executed directly by users or shell scripts
- **/boot**
   - *vmlinuz-linux* compressed image of the kernel. It gets uncompressed, loaded into memory, and executed at boot
   - **/boot/grub**
- **/media** Removable mounting point like usb stick
- **/mnt** temporary mounting. This directory is generally used for mounting filessytems temporarily when needed.
- **/srv/**
   - **/srv/http/** or **/srv/ftp/** mostly used for to serve file for *apache* or *ftp* server
- **/run** This directory contains system information data describing the system since it was booted. Files under this directory must be cleared at the beginning of the boot process.