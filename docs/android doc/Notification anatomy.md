---
layout: default
parent: android doc
title: Notification anatomy
---

## Notification anatomy

The design of a notification is determined by system templates—your app simply defines the contents for each portion of the template. Some details of the notification appear only in the expanded view.

![](media/notification-callouts_2x.png)

**Figure 7.** A notification with basic details

The most common parts of a notification are indicated in figure 7 as follows:

1.  Small icon: This is required and set with `[setSmallIcon()](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setSmallIcon(int))`.
2.  App name: This is provided by the system.
3.  Time stamp: This is provided by the system but you can override with `[setWhen()](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setWhen(long))` or hide it with `[setShowWhen(false)](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setShowWhen(boolean))`.
4.  Large icon: This is optional (usually used only for contact photos; do not use it for your app icon) and set with `[setLargeIcon()](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setLargeIcon(android.graphics.Bitmap))`.
5.  Title: This is optional and set with `[setContentTitle()](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setContentTitle(java.lang.CharSequence))`.
6.  Text: This is optional and set with `[setContentText()](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setContentText(java.lang.CharSequence))`.
