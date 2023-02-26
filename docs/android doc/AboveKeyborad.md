---
layout: default
parent: android doc
title: AboveKeyborad
---
# AboveKeyborad
### for activity

add this to manifest -> activity
```xml
android:windowSoftInputMode="adjustResize"  
```

and then this to layout
```xml 
android:fitsSystemWindows="true"  

```

### for bottom sheet
set this style to bottom sheet dialog
```xml

<style name="DialogStyle" parent="Theme.MaterialComponents.DayNight.DarkActionBar">  
 <item name="android:windowIsFloating">false</item>  
 <item name="android:statusBarColor">@android:color/transparent</item>  
 <item name="android:windowSoftInputMode">adjustResize</item>  
</style>
```
```java 
  setStyle(DialogFragment.STYLE_NORMAL, R.style.DialogStyle);

```