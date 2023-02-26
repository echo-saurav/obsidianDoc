---
layout: default
parent: android doc
title: Basic activity with viewbind
---
# Basic activity with viewbind
```java 
public class MainActivity extends AppCompatActivity {
    private CreateAccountActivityBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding=CreateAccountActivityBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
    }
}
```

