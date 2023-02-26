---
layout: default
parent: android doc
title: JetpackNavigation
---

### Dependency
```gradle 
    def nav_version = "2.3.5"

  // Java language implementation
  implementation "androidx.navigation:navigation-fragment:$nav_version"
  implementation "androidx.navigation:navigation-ui:$nav_version"

  // Kotlin
  implementation "androidx.navigation:navigation-fragment-ktx:$nav_version"
  implementation "androidx.navigation:navigation-ui-ktx:$nav_version"

  // Feature module Support
  implementation "androidx.navigation:navigation-dynamic-features-fragment:$nav_version"

  // Testing Navigation
  androidTestImplementation "androidx.navigation:navigation-testing:$nav_version"

  // Jetpack Compose Integration
  implementation "androidx.navigation:navigation-compose:2.4.0-beta02"

```


## navigaton with bottom navigation 
### add this to activity layout
```java 
  
    <androidx.fragment.app.FragmentContainerView
        android:id="@+id/nav_host_fragment"
        android:name="androidx.navigation.fragment.NavHostFragment"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_above="@+id/bottom_nav"
        app:defaultNavHost="true"
        app:navGraph="@navigation/main_activity_navigation" />

```
```java 
  NavHostFragment navHostFragment =
                (NavHostFragment) getSupportFragmentManager().findFragmentById(binding.navHostFragment.getId());
        NavController navController = navHostFragment.getNavController();
        NavigationUI.setupWithNavController(binding.bottomNav, navController);

```


change navigation
```java 
Bundle bundle = new Bundle(); // for passing args
Navigation.findNavController(view).navigate(R.id.action_home_to_detailsFragment,
                            bundle);

from a fragment

NavHostFragment.findNavController(this).navigate(R.id.action_loginFragment_to_regFragment);

```

example navigation graph
```java 
      <fragment
        android:id="@+id/profile"
        android:name="com.sindabad.sindabadodoo.home.fragments.ProfileFragment"
        android:label="Profile"
        tools:layout="@layout/profile_fragment">
        <action
            android:id="@+id/action_profile_to_loginFragment"
            app:destination="@id/loginFragment"
            app:popUpTo="@id/main_nav"
            app:popUpToInclusive="true"

            app:enterAnim="@anim/fragment_fade_enter"
            app:popExitAnim="@anim/fragment_fade_exit"
            />
        <action
            android:id="@+id/action_profile_to_detailsFragment2"
            app:destination="@id/detailsFragment" />
    </fragment>

```

### Navigational with other navigation component
bottom navigation example
```java 
          //
        NavHostFragment navHostFragment =
                (NavHostFragment) getSupportFragmentManager().findFragmentById(binding.navHostFragment.getId());
        NavController navController = navHostFragment.getNavController();
        NavigationUI.setupWithNavController(binding.bottomNav, navController);

```

