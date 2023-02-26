---
layout: default
parent: android doc
title: FirebaseNotification
---
Make service to get notification from firebase
```java
<service  
 android:name=".services.PushNotification"  
 android:exported="false">  
 <intent-filter>  
 <action android:name="com.google.firebase.MESSAGING_EVENT" />  
 </intent-filter>  
</service>

```
PushNotification 
```java 
  public class PushNotification extends FirebaseMessagingService {
    private String channelId = "Post notifications";
    private NotificationManager mNotificationManager;
    @Override
    public void onNewToken(String token) {
        super.onNewToken(token);
        Firebase.updateFcmToken(token);
    }

    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);
        Log.d("MY_LOG", "onMessageReceived: "+remoteMessage.getData());
        int requestID = (int) System.currentTimeMillis();
        String message=remoteMessage.getData().get("title");
        String description=remoteMessage.getData().get("title");
        Intent intent=new Intent(getApplicationContext(), SplashActivity.class);
        showNotification(intent,message,description,requestID);
        
    }
  }


```

Start app with initializing fcm token
```java 
  public class Init extends Application {

    private static final String TAG = "MY_LOG";

    @Override
    public void onCreate() {
        super.onCreate();

        FirebaseUser user= FirebaseAuth.getInstance().getCurrentUser();
        if(user!=null){
            FirebaseInstanceId.getInstance().getInstanceId()
                    .addOnCompleteListener(task -> {
                        if (!task.isSuccessful()) {
                            Log.w(TAG, "getInstanceId failed", task.getException());
                            return;
                        }
                        // Get new Instance ID token
                        String token = task.getResult().getToken();

                        Firebase.updateFcmToken(token);

                    });

            FirebaseMessaging.getInstance().subscribeToTopic("all");
        }
    }
}


```

