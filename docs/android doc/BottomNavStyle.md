
### Bottom nav style
```xml 
    <com.google.android.material.bottomnavigation.BottomNavigationView
        app:itemIconSize="27dp"
        app:itemBackground="@drawable/bottom_selection"
        app:labelVisibilityMode="unlabeled"
        app:itemHorizontalTranslationEnabled="false"
        android:id="@+id/bottom_navigation"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        app:itemIconTint="@android:color/black"
        app:itemTextColor="@android:color/black"
        app:menu="@menu/bottom_navigation_menu" />  

```
Add bottom selection style if i want to modify it
```xml 
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@color/colorPrimary" android:state_checked="true">
    </item>

    <item android:drawable="@android:color/white" android:state_checked="false">
    </item>
</selector>

```