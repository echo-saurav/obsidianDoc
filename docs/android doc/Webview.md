---
layout: default
parent: android doc
title: Webview
---
# Webview
### Simple webview
```java 
		webView=findViewById(R.id.web_view);
        webView.getSettings().setJavaScriptEnabled(true);
        webView.loadUrl("google.com");
        webView.setWebViewClient(new WebClient());
```

### Load asset html
```java
	webView.loadUrl("file:///android_asset/index.html");
```

### Web client
```java 
  

    private class WebClient extends WebViewClient {

        @Override
        public void onPageCommitVisible(WebView view, String url) {
            super.onPageCommitVisible(view, url);

//            if(progressBar.getVisibility()== View.VISIBLE){
//                progressBar.setVisibility(View.GONE);
//            }
            if(swipeRefreshLayout.isRefreshing()){
                swipeRefreshLayout.setRefreshing(false);
            }
        }

        @Override
        public void onPageStarted(WebView view, String url, Bitmap favicon) {
            super.onPageStarted(view, url, favicon);
//            if(progressBar.getVisibility()==View.GONE){
//                progressBar.setVisibility(View.VISIBLE);
//            }
            if(!swipeRefreshLayout.isRefreshing()){
                swipeRefreshLayout.setRefreshing(true);
            }
        }

        @Override
        public boolean shouldOverrideUrlLoading(WebView view, String url) {
            view.loadUrl(url);
            return true;
        }
    }

```
