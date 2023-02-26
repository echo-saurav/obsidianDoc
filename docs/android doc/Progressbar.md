---
layout: default
parent: android doc
title: Progressbar
---
```java 
  		ProgressDialog progressDialog = new ProgressDialog(this);
        progressDialog.setTitle("Fetching data");
        progressDialog.setMessage("Please wait, getting user information");
        progressDialog.setCancelable(false);
        progressDialog.show();

```