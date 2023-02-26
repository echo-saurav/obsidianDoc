---
layout: default
parent: android doc
title: Ripple
---
# Ripple


```xml 
<?xml version="1.0" encoding="utf-8"?>
<ripple xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:color="@color/colorPrimary">
    <item android:id="@android:id/mask">
        <shape android:shape="rectangle">
            <solid android:color="@color/colorPrimary" />
            <corners android:radius="13sp" />
        </shape>
    </item>

    <item android:id="@android:id/background">
        <shape android:shape="rectangle">
            <solid android:color="@color/colorPrimaryDark"/>
            <corners android:radius="17sp" />
        </shape>
    </item>
</ripple>

```