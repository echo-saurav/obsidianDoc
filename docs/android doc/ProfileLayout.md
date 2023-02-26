---
layout: default
parent: android doc
title: ProfileLayout
---

```java
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <LinearLayout
        android:padding="10dp"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <RelativeLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content">

            <androidx.cardview.widget.CardView
                app:cardElevation="0dp"
                android:layout_width="100dp"
                android:layout_height="100dp"
                android:layout_centerHorizontal="true"
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
        </RelativeLayout>

        <TextView
            android:id="@+id/title"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center_horizontal"
            android:layout_marginTop="10dp"
            android:text="Title"
            android:textSize="20dp"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/subtitle"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center_horizontal"
            android:text="Subtitle" />

		
    </LinearLayout>


</ScrollView>

```