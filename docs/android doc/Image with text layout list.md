---
layout: default
parent: android doc
title: Image with text layout list
---
# Image with text layout list

# Image with text list
```java
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="20px">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Heading"
        android:textSize="20dp"
        android:textStyle="bold" />

    <!-- home click-->
    <LinearLayout
        android:id="@+id/home"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_vertical"
        android:orientation="horizontal">

        <ImageView
            android:layout_width="50dp"
            android:layout_height="50dp"
            android:src="@drawable/home_icon" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginStart="10sp"
            android:text="Home" />
    </LinearLayout>

    <!-- Profile click-->
    <LinearLayout
        android:id="@+id/profile"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_vertical"
        android:orientation="horizontal">

        <ImageView
            android:layout_width="50dp"
            android:layout_height="50dp"
            android:src="@drawable/person_icon" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginStart="10sp"
            android:text="Person" />
    </LinearLayout>


</LinearLayout>

```