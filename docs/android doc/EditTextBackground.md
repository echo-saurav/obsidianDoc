```java 
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_focused="true" android:drawable="@drawable/edit_text_focused"/>
    <item android:drawable="@drawable/edit_text_not_focused"/>
</selector>

```


```java 
  <?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item>
        <shape android:shape="rectangle">
            <solid android:color="@color/light_gray"/>
            <corners android:radius="@dimen/small_size" />
        </shape>
    </item>
</selector>

```

```java 
  <?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item>
        <shape android:shape="rectangle">
            <solid android:color="@android:color/darker_gray"/>
            <corners android:radius="@dimen/small_size" />
        </shape>
    </item>
</selector>

```