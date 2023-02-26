---
layout: default
parent: android doc
title: Bottomsheet navigation
---

# Code
```java 
  

public class BottomSheetNavFragment extends BottomSheetDialogFragment {
    private OnClickItem item;
    private BottomSheetLayoutBinding binding;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        binding = BottomSheetLayoutBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        binding.home.setOnClickListener(v -> {
            item.onClickItem(0);
            dismiss();
        });
        binding.profile.setOnClickListener(v -> {
            item.onClickItem(1);
            dismiss();
        });

    }


    public static BottomSheetNavFragment getInstance(OnClickItem onClickItem) {
        return new BottomSheetNavFragment(onClickItem);
    }

    BottomSheetNavFragment(OnClickItem onClickItem) {
        this.item = onClickItem;
    }


    public interface OnClickItem {
        void onClickItem(int id);
    }
}

```


# On activity

```java 
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.bottom_sheet_nav_layout);

        homeFragment = new HomeFragment();
        profileFragment = new ProfileFragment();

        initialFragment(homeFragment);

        findViewById(R.id.button).setOnClickListener(view -> {
            BottomSheetNavFragment.getInstance(id -> {
                if (id == 0) {
                    replaceFragment(homeFragment);
                } else if (id == 1) {
                    replaceFragment(profileFragment);
                }
            }).show(getSupportFragmentManager(), "bottom");
        });
    }

```


### round Style
```java 
	
    <style name="AppBottomSheetDialogTheme" parent="Theme.Design.Light.BottomSheetDialog">
        <item name="bottomSheetStyle">@style/AppModalStyle</item>
    </style>

    <style name="AppModalStyle" parent="Widget.Design.BottomSheet.Modal">
        <item name="android:background">@drawable/rounded_dialog</item>
    </style>

```

drawable
```java 
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <solid android:color="@android:color/white"/>
    <corners android:topLeftRadius="16dp"
        android:topRightRadius="16dp"/>
</shape>

```