---
layout: default
parent: android doc
title: Tab layout navigation
---

# xml
```java
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <androidx.viewpager.widget.ViewPager
        android:id="@+id/view_pager"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_above="@+id/tab_layout" />

    <com.google.android.material.tabs.TabLayout
        android:id="@+id/tab_layout"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        app:tabMode="scrollable" />
</RelativeLayout>

```

# Code

```java 
  public class TabNavActivity extends AppCompatActivity {
    private TabNavLayoutBinding binding;
    private List<FragmentValue> fragments;
    private Fragment homeFragment, profileFragment;


    class FragmentValue {
        Fragment fragment;
        String title;

        public FragmentValue(Fragment fragment, String title) {
            this.fragment = fragment;
            this.title = title;
        }
    }

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = TabNavLayoutBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        binding.tabLayout.setupWithViewPager(binding.viewPager);

        homeFragment = new HomeFragment();
        profileFragment = new ProfileFragment();

        fragments = new ArrayList<>();
        fragments.add(new FragmentValue(homeFragment, "Home"));
        fragments.add(new FragmentValue(profileFragment, "Profile"));

        binding.viewPager.setAdapter(new TabHomeAdapter(getSupportFragmentManager()));

    }

    class TabHomeAdapter extends FragmentStatePagerAdapter {

        public TabHomeAdapter(@NonNull FragmentManager fragmentManager) {
            super(fragmentManager);
        }

        @NonNull
        @Override
        public Fragment getItem(int position) {
            return fragments.get(position).fragment;
        }


        @Nullable
        @Override
        public CharSequence getPageTitle(int position) {
            return fragments.get(position).title;
        }

        @Override
        public int getCount() {
            return fragments.size();
        }
    }
}


```