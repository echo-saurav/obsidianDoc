---
layout: default
title: pm2
---
## Gen config file

```bash
 pm2 init simple
```

## My template file for `ecosystem.config.js`:
[PM2 - Ecosystem File configs](https://pm2.keymetrics.io/docs/usage/application-declaration/) 

```js
module.exports = {
  apps : [{
		name: "discordbot",
		script: "./src/main.py",
		// args: "run build",
		watch: ["src"],
		watch_delay: 10000,
		autorestart: true,
		restart_delay: 3000,
		log_file: "./logs.log",
		time: true,
		merge_logs: true,
		max_memory_restart: "300M",
		instances: 1,
		exec_mode: "fork"
  }]
}
```

## scripts for restarting 
```bash
#!/bin/bash

npm run build
exit_code=$?

if [ $exit_code -eq 0 ]; then
	echo "success"

	while true; do
		sleep 1
	done

else
	echo "error"
	exit $exit_code
fi
```


## To start app on boot
```bash
pm2 startup
## after running outputed command
pm2 save
```

## Commands
```bash
# Start all applications
pm2 start ecosystem.config.js
```
```bash
# Stop all
pm2 stop ecosystem.config.js
```
```bash
# Restart all
pm2 restart ecosystem.config.js
```
```bash
# Reload all
pm2 reload ecosystem.config.js
```
```bash
# Delete all
pm2 delete ecosystem.config.js
```





