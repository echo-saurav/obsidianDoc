# With Viewbinding
```java 
class HomeFragment extends Fragment {
	private BottomSheetMenuPickerBinding binding;
	
	
	@Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        binding = BottomSheetMenuPickerBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

    }
}

```

## Initial fragment
```java 
  
class HomeFragment extends Fragment {
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.home, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

    }
}

```



### Replace freagment function

```java
   private void replaceFragment(Fragment fragment) {
        FragmentManager mFragmentManager = getSupportFragmentManager();
        FragmentTransaction fragmentTransaction = mFragmentManager.beginTransaction();
        fragmentTransaction.replace(R.id.frame, fragment, null);
        fragmentTransaction.commit();
    }
```

### add this to back stacking
```java
fragmentTransaction.addToBackStack(null);
```

### Restore backstack state
```java 
  
    private void replaceFragment(Fragment fragment) {
        String backStateName = fragment.getClass().getName();
        FragmentManager manager = getSupportFragmentManager();
        FragmentTransaction ft = manager.beginTransaction();
        ft.setCustomAnimations(android.R.anim.fade_in, android.R.anim.fade_out);
        //if it profile fragment
        if (backStateName.equals(ProfileFragment.class.getName())) { //fragment not in back stack, create it.
            ft.replace(R.id.frame, fragment);
            ft.addToBackStack(backStateName);
            ft.commit();
        } else {

            boolean fragmentPopped = manager.popBackStackImmediate(backStateName, 0);
            if (!fragmentPopped) { //fragment not in back stack, create it.

                ft.replace(R.id.frame, fragment);
                ft.addToBackStack(backStateName);
                ft.commit();
            }
        }
    }

```