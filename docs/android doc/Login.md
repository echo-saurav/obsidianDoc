---
layout: default
parent: android doc
title: Login
---
# Login

# Login methods


### login layout xml
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
            android:hint="password"/>

        <TextView
            android:id="@+id/forget_pass_button"
            android:textStyle="bold"
            android:padding="10dp"
            android:layout_gravity="right"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="forget password?"/>


        <Button
            android:id="@+id/login_button"
            android:textAllCaps="false"
            android:layout_marginTop="20dp"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Login"/>
    </LinearLayout>


    <LinearLayout
        android:layout_marginBottom="20dp"
        android:layout_alignParentBottom="true"
        android:id="@+id/home"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center"
        android:orientation="horizontal">

        <TextView
            android:paddingTop="6dp"
            android:textStyle="bold"
            android:layout_gravity="right"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Don't have account?"/>

        <TextView
            android:id="@+id/create_new_account_button"
            android:textColor="@color/purple_700"
            android:padding="6dp"
            android:textStyle="bold"
            android:layout_gravity="right"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="create new account"/>
    </LinearLayout>

</RelativeLayout>

```


Code for login as starting page 
```java 
  public class LoginActivity extends AppCompatActivity {
    private LoginActivityBinding binding;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = LoginActivityBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        binding.loginButton.setOnClickListener(view ->checkInput());

        binding.forgetPassButton.setOnClickListener(view -> {
            startActivity(new Intent(this,ResetPassActivity.class));
        });

        binding.createNewAccountButton.setOnClickListener(view -> {
            startActivity(new Intent(this,CreateAccountActivity.class));
        });

    }

    private void checkInput() {

        if (binding.email.getText().toString().isEmpty() || binding.pass.getText().toString().isEmpty()) {
            Toast.makeText(this, "Please enter email and pass", Toast.LENGTH_LONG).show();
        } else {
            Repository.getInstance().login(binding.email.getText().toString().trim(), binding.pass.getText().toString().trim(),this);
        }

    }

}


```