#coding  
[termux-services](https://github.com/termux/termux-services) contains a set of scripts for controlling services. Instead of putting commands in ~/.bashrc or ~/.bash\_profile, they can be started and stopped with termux-services.

Only a few packages so far contain the necessary service scripts, these are:

-   [emacsd](https://github.com/termux/termux-packages/blob/e0b7d90428d70b0c6e727803eb8d70299691d364/packages/emacs/build.sh#L88)
-   [ftpd](https://github.com/termux/termux-packages/blob/aafb83e37bb33c35ae6dbeb40d6854da69b00f1b/packages/busybox/build.sh#L71)
-   [ipfs](https://github.com/termux/termux-packages/blob/c7b24366f699e58d19869716d6cae4fbffa3657f/packages/ipfs/build.sh#L9)
-   [mpd](https://github.com/termux/termux-packages/blob/246ac85ae0595d7dcb701c13a52610b66247c8a0/packages/mpd/build.sh#L38)
-   [sshd](https://github.com/termux/termux-packages/blob/aafb83e37bb33c35ae6dbeb40d6854da69b00f1b/packages/openssh/build.sh#L90)
-   [telnetd](https://github.com/termux/termux-packages/blob/aafb83e37bb33c35ae6dbeb40d6854da69b00f1b/packages/busybox/build.sh#L71)
-   [tor](https://github.com/termux/termux-packages/blob/c1737592010d32be147d22920ddb617545909e01/packages/tor/build.sh#L21)
-   [transmission](https://github.com/termux/termux-packages/blob/e60040365440a101e4cc4afaa810f12b0cf6e0b6/packages/transmission/build.sh#L22)

  
To install termux-services, run

pkg install termux-services

and then restart termux so that the service-daemon is started.

To then enable and run a service, run

sv-enable <service>

If you only want to run it once, run

sv up <service>

To later stop a service, run:

sv down <service>

Or to disable it

sv-disable <service>

A service is disabled if \`$PREFIX/var/service/<service>/down\` exists, so the \`sv-enable\` and \`sv-disable\` scripts touches, or removes, this file.

termux-services uses the programs from [runit](http://smarden.org/runit/) to control the services. A bunch of example scripts are available from the [same site](http://smarden.org/runit/runscripts.html). If you find a script you want to use, or if you write your own, you can use set it up by running:

mkdir -p $PREFIX/var/service/<PKG>/log
ln -sf $PREFIX/share/termux-services/svlogger $PREFIX/var/service/<PKG>/log/run

and then put your run script for the package at $PREFIX/var/service/<PKG>/run and make sure that it is runnable.

You can then run

sv up <PKG>

to start it.

Log files for services are situated in $PREFIX/var/log/sv/<PKG>/ with the active log file named "current".