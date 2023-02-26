---
layout: default
title: Cronjob
---
# Linux cronjob
need to install the package then start the service `cronie.service` , to add service `cronie -e`


## Termux cronjob
Use crontab as usual you use in any Linux, but some limitations in case your android kills termux app otherwise crontab work great.
[Termux projects](projects/Termux%20projects.md) 

```bash
pkg install cronie termux-services
sv-enable crond
crontab -e 
```

it will open default text editor , write your job in it and save it,

For example :

```bash
* * * * * mkdir ~/crontab-testing
```

this cron job run every minute and create that.directory .
Now you have to learn crontab formatting, [https://crontab.guru/](https://crontab.guru/)

- daily cron `0 0 * * *`
- every hour `0 * * * *`

cheatsheet
![](docs/media/croncheatsheet.jpeg)

## cronjob syntext site 
<iframe width="100%" height="500px" src="https://crontab.guru/" class="resize-vertical"></iframe> 

