---
layout: default
title: Useful Scripts
---
# Useful Scripts
#linux 


1.	Download youtube audio ``youtube-dl -t --extract-audio --audio-format mp3 %url``
2.	Get window name ``	xprop |awk '/WM\_CLASS/{print $4}'  ``
3.	Get input code ``	xev  ``
4.	Hardware name ``sudo dmidecode -t 2  ``
5.	Loop youtube video ``document.getElementsByClassName("video-stream html5-main-video")\[0\].lo  
op=false


## Automate Keypress
```bash
# start recording macro
xmacrorec2 > yourfile.txt
# play macro
xmacroplay "$DISPLAY" < yourfile.txt
```











