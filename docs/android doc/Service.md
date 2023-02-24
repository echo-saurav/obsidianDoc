# Service
```java 
  public class BackgroundTask extends Service {
	
	@Override
    public void onCreate() {
        super.onCreate();
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {

		// sticky make not killable service
        return START_STICKY;
    }
	  
	@Override
    public void onDestroy() {
        super.onDestroy();
		// destroy everything that can cause app crash
    }
  
  }

```