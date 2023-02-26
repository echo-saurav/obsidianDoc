---
layout: default
parent: android doc
title: Thread
---
# Thread

```java 
        long milisec = 1000;
        Handler handler = new Handler();
        Runnable runnable = () -> {
			// background tasks
        };
        handler.postDelayed(runnable, milisec * 15); // 15 secound 

```