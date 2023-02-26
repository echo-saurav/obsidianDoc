---
layout: default
parent: android doc
title: ForegroundService
---

```java 
    private void startForegroundService() {
        String channelName = "Tracking activity";
        NotificationChannel chan = null;
        ///
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            chan = new NotificationChannel(NOTIFICATION_CHANNEL_ID, channelName, NotificationManager.IMPORTANCE_NONE);
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            chan.setLightColor(Color.BLUE);
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            chan.setLockscreenVisibility(Notification.VISIBILITY_PRIVATE);
        }
        NotificationManager manager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        assert manager != null;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            manager.createNotificationChannel(chan);
        }

        Notification notification=getNotification();
        startForeground(2, notification);
    }

    private Notification getNotification(){
        Intent intent = new Intent(this, SplashActivity.class);
        PendingIntent pi = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT);
        NotificationCompat.Builder notification = new NotificationCompat.Builder(this, NOTIFICATION_CHANNEL_ID);
        notification
                .setSubText("Tracking user")
                .setSmallIcon(R.mipmap.ic_launcher_round)
                .setOngoing(true)
                .setContentIntent(pi)
                .setPriority(NotificationCompat.PRIORITY_MIN) //MIN so it's not shown in the status bar before Oreo, on Oreo it will be bumped to LOW
                .setShowWhen(false)
                .setAutoCancel(false);
        notification.setGroup("BackgroundService");

        return notification.build();
    }

```

Start this from a service to run it in the background
```java 
	private Runnable runnable;
    private Handler handler;
	private long second = 60;
	private long milliSecond =1000;


      @Override
    public int onStartCommand(Intent intent, int flags, int startId) {

        this.handler = new Handler();
        runnable = () -> {
            tick(); // actual task
            handler.postDelayed(runnable, milliSecond* second);
        };
        handler.post(runnable);

        startForegroundService();
        return START_STICKY;
    }

  @Override
    public void onDestroy() {
        super.onDestroy();
        Log.d(TAG, "onDestroy: service destroying");
        if(runnable!=null){
            handler.removeCallbacks(runnable);
        }
    }

```