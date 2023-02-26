---
layout: default
parent: android doc
title: Splash Screen
---
# App Start
### Splash screen background
```java
  
<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android" >

    <item android:drawable="@android:color/black"/>
    <item>
        <bitmap
            android:gravity="center"
            android:src="@drawable/sp" />
    </item>

</layer-list>
```

### Splash theme
Set theme on manifest file, then change it on splash activity. then start other main activity
```java
  
    <style name="splashTheme" parent="Theme.AppCompat.Light.NoActionBar">
        <item name="android:windowBackground">@drawable/splash_drawable</item>
    </style>

```
another theme for splash
```java 
      <style name="SplashTheme" parent="Theme.SindabadOdoo">
        <item name="android:windowTranslucentStatus" tools:targetApi="kitkat">true</item>
        <item name="android:windowTranslucentNavigation" tools:targetApi="kitkat">true</item>
        <item name="android:windowDisablePreview">false</item>
        <item name="android:windowBackground">@drawable/splash_background</item>
    </style>

```