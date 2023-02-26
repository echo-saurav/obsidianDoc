---
layout: default
parent: android doc
title: CreateAccount
---
# CreateAccount

 ### xml 
```java
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <LinearLayout
        android:padding="10dp"
        android:layout_centerInParent="true"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">
        <TextView
            android:layout_marginBottom="20dp"
            android:textSize="20sp"
            android:layout_gravity="center"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/app_name"/>
        <EditText
            android:maxLines="1"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:id="@+id/username"
            android:hint="username"/>
        <EditText
            android:maxLines="1"
            android:inputType="textEmailAddress"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:id="@+id/email"
            android:hint="email"/>
        <EditText
            android:maxLines="1"
            android:inputType="textPassword"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:id="@+id/pass"
            android:hint="password (at least 6 character)"/>
        <EditText
            android:maxLines="1"
            android:inputType="textPassword"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:id="@+id/pass2"
            android:hint="re-enter password"/>

        <Button
            android:id="@+id/create_account"
            android:textAllCaps="false"
            android:layout_marginTop="20dp"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="create account"/>
    </LinearLayout>

</RelativeLayout>

```
 
 
 ### Check input and create account
 ```java 
     private void checkInput() {
        // if any of the field is empty
        if (binding.username.getText().toString().isEmpty() ||
                binding.email.getText().toString().isEmpty() ||
                binding.pass.getText().toString().isEmpty() ||
                binding.pass2.getText().toString().isEmpty()) {
            Toast.makeText(this, "Please enter all the fields", Toast.LENGTH_LONG).show();
            return;
        }
        // check min pass character
        int minPassChar = 6;
        if (!(binding.pass.getText().toString().length() >= minPassChar)) {
            Toast.makeText(this, "Enter at least " + minPassChar + " character long password", Toast.LENGTH_LONG).show();
            return;
        }

        // check if password matched
        if (!binding.pass.getText().toString().equals(binding.pass2.getText().toString())) {
            Toast.makeText(this, "Password not matched", Toast.LENGTH_LONG).show();
            binding.pass2.setText("");
            return;
        }

        // if everything worked out
        Repository.getInstance().createAccount(binding.username.getText().toString().trim(),
                binding.email.getText().toString().trim(),
                binding.pass.getText().toString().trim(), this);
    }

```


