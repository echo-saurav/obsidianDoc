---
layout: default
parent: android doc
title: Common function for navigation
---

# Initial Fragment
```java 
 // initial fragment setup
    private void initialFragment(Fragment fragment){
        FragmentTransaction fragmentTransaction;
        fragmentTransaction = getSupportFragmentManager().beginTransaction();
        fragmentTransaction.setCustomAnimations(android.R.anim.fade_in, android.R.anim.fade_out);
        fragmentTransaction.add(R.id.frame, fragment, fragment.getClass().getName());
        fragmentTransaction.commit();
    }

```

# Change/replace Fragment

```java 

     private void replaceFragment(Fragment fragment) {
        FragmentManager mFragmentManager = getSupportFragmentManager();
        FragmentTransaction fragmentTransaction = mFragmentManager.beginTransaction();
        fragmentTransaction.replace(R.id.frame, fragment, null);
        fragmentTransaction.commit();
    }

```