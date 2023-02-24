
# Bottom Navigation


```java 
  
public class MainActivity extends AppCompatActivity implements NavigationBarView.OnItemReselectedListener {
    private BottomNavigationView bottomNavigationView;
    private HomeFragment homeFragment;
    private ProfileFragment profileFragment;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bottomNavigationView = findViewById(R.id.bottom_nav);
        bottomNavigationView.setOnItemReselectedListener(this);

        homeFragment = new HomeFragment();
        profileFragment = new ProfileFragment();
        FragmentTransaction fragmentTransaction;
        fragmentTransaction = getSupportFragmentManager().beginTransaction();
        fragmentTransaction.setCustomAnimations(android.R.anim.fade_in, android.R.anim.fade_out);
        fragmentTransaction.add(R.id.frame, homeFragment, homeFragment.getClass().getName());
        fragmentTransaction.commit();
    }

    @Override
    public void onNavigationItemReselected(@NonNull MenuItem item) {
        if (item.getItemId() == R.id.home) {
            replaceFragment(profileFragment);
        } else if (item.getItemId() == R.id.profile) {
            replaceFragment(profileFragment);
        }
    }

    private void replaceFragment(Fragment fragment) {
        FragmentManager mFragmentManager = getSupportFragmentManager();
        FragmentTransaction fragmentTransaction = mFragmentManager.beginTransaction();
        fragmentTransaction.add(R.id.frame, fragment, null);
        fragmentTransaction.commit();
    }
}
```

### Set image on bottom nav
```java 
  bottomNavigationView.getMenu().findItem(R.id.profile).setIcon(mBitmapDrawable);

```
set from picaso lib 
[[Programming/Images#circle image with picaso]]
```java 
        Target target;
        target = new Target() {
            @Override
            public void onBitmapLoaded(Bitmap bitmap, Picasso.LoadedFrom from) {
                BitmapDrawable mBitmapDrawable = new BitmapDrawable(getResources(), bitmap);
                bottomNavigationView.getMenu().findItem(R.id.profile).setIcon(mBitmapDrawable);
            }

            @Override
            public void onBitmapFailed(Exception e, Drawable errorDrawable) {

            }

            @Override
            public void onPrepareLoad(Drawable placeHolderDrawable) {
            }
        };


		Picasso.get().load(imageUrl).error(R.drawable.person_icon)
                            .transform(new CircleTransform())
                            .into(target);


```