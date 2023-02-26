---
layout: default
parent: android doc
title: Swipe to refresh
---
### Dependency
```
	implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
```
### Swipe to refrsh web page 

```java 
	SwipeRefreshLayout swipeRefreshLayout;
	swipeRefreshLayout=findViewById(R.id.swipe_to_refresh);
  	swipeRefreshLayout.setOnRefreshListener(() -> {
            webView.reload();
    });

```


### webview swipe to refresh
```java 
 swipeRefreshLayout.getViewTreeObserver().addOnScrollChangedListener(() -> swipeRefreshLayout.setEnabled((webView.getScrollY() == 0)));
        swipeRefreshLayout.setOnRefreshListener(() -> {
            webView.reload();
});

```

