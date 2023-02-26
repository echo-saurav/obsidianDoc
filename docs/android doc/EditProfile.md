---
layout: default
parent: android doc
title: EditProfile
---
# EditProfile
```java 
  <?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <androidx.appcompat.widget.Toolbar
        android:id="@+id/toolbar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        app:title="Edit Profile"/>

    <LinearLayout
        android:layout_below="@+id/toolbar"
        android:layout_marginTop="10dp"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:layout_margin="10dp">
        <androidx.cardview.widget.CardView
            app:cardElevation="0dp"
            android:layout_width="100dp"
            android:layout_height="100dp"
            android:layout_marginTop="20dp"
            app:cardCornerRadius="50dp">

            <ImageView
                android:layout_gravity="center"
                android:scaleType="centerCrop"
                android:id="@+id/image_view"
                android:layout_width="103dp"
                android:layout_height="103dp"
                android:src="@mipmap/ic_launcher_round" />
        </androidx.cardview.widget.CardView>



        <EditText
            android:id="@+id/username"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginBottom="7sp"
            android:maxLines="1"
            android:padding="13sp"
            android:hint="Username"
            android:textSize="17sp" />
        <EditText
            android:id="@+id/bio"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginBottom="7sp"
            android:maxLines="1"
            android:padding="13sp"
            android:hint="Bio"
            android:textSize="17sp" />
    </LinearLayout>

    <Button
        android:id="@+id/update_button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        android:layout_centerHorizontal="true"
        android:layout_marginStart="10dp"
        android:layout_marginTop="10dp"
        android:layout_marginEnd="10dp"
        android:layout_marginBottom="10dp"
        android:text="Update Profile"
        android:textAllCaps="false"
        android:textColor="@android:color/white" />

</RelativeLayout>

```