---
layout: default
parent: android doc
title: ChatLayout
---
This is for reverse chat layout recycler view
```java 
  LinearLayoutManager linearLayoutManager = new LinearLayoutManager(this);
        linearLayoutManager.setReverseLayout(true);
        linearLayoutManager.getStackFromEnd();

```