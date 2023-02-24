module.exports = {
  apps: [
    {
      name: "obsidianDoc",
      script: "./RunSchedule.sh",
      cron_restart: '0 9,17 * * *',
      // args: "run build",
      //watch: ["src","public"],
      watch: false,
      //ignore_watch: ["node_modules"],
      //watch_delay: 1000,
      autorestart: true,
      restart_delay: 3000,
      log_file: "./logs.log",
      time: true,
      merge_logs: true,
      // max_memory_restart: "300M",
      instances: 1,
      exec_mode: "fork"
    },
  ],
};
