---
layout: default
parent: android doc
title: DrawableCollection
---


### Round stroke 
```xml 
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <corners android:radius="13dp"/>
    <stroke android:color="@color/colorPrimaryDark"
        android:width="1dp"/>
</shape>

```

### Round solid
```xml 
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <corners android:radius="13dp"/>
    <solid android:color="@color/colorPrimaryDark"
        android:width="1dp"/>
</shape>

```

### Doted box
```xml 
  
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <stroke
        android:color="#C7B299"
        android:dashWidth="10px"
        android:dashGap="10px"
        android:width="1dp"/>
</shape>
```