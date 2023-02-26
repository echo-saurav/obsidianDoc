---
layout: default
parent: android doc
title: EditText
---
### Text Suggestion
```java 
    String[] foods = getResources().getStringArray(R.array.food_item_list);
        ArrayAdapter<String> autoComplateTextView = new ArrayAdapter<String>
                (this,android.R.layout.simple_list_item_1,foods);
        foodNameEditText.setAdapter(autoComplateTextView);

```

### Text listener
```java 
        searchEditText = findViewById(R.id.search);
        searchEditText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
            }

            @Override
            public void afterTextChanged(Editable s) {
                search(searchEditText.getText().toString().toLowerCase());
            }
        });

```

## Material text field
```java
<com.google.android.material.textfield.TextInputLayout  
 style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"  
 android:layout_marginTop="10dp"  
 android:id="@+id/gen"  
 android:layout_width="match_parent"  
 android:layout_height="wrap_content"  
 android:hint="Gender ">  
  
 <com.google.android.material.textfield.TextInputEditText  
 android:layout_width="match_parent"  
 android:layout_height="wrap_content" />  
  
</com.google.android.material.textfield.TextInputLayout>
```