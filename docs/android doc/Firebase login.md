---
layout: default
parent: android doc
title: Firebase login
---
# Firebase user management
### Create new user
```java 

    void signUp(String name, String email, String password) {
        progressDialog.show();
        mAuth.createUserWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        setProfile(name, email);

                    } else {
                        progressDialog.dismiss();
                        Toast.makeText(getActivity(), task.getException().getMessage(), Toast.LENGTH_LONG).show();
                    }
                });
    }

```


### Login with email
```java 
    private FirebaseAuth mAuth;
	// mAuth =FirebaseAuth.getInstance(); setup firebase auth
 

    void loginWithEmail(String email, String password) {
        progressDialog.show();
        mAuth.signInWithEmailAndPassword(email,password)
                .addOnCompleteListener(task -> {
                    if(task.isSuccessful()){
                        if(FirebaseAuth.getInstance().getCurrentUser().isEmailVerified()){
                            afterLogin(getActivity(),progressDialog);
                        }else {
                            progressDialog.dismiss();
                            Toast.makeText(getContext(),"Please verify your email",Toast.LENGTH_LONG).show();
                        }
                    }else {
                        progressDialog.dismiss();
                        Toast.makeText(getContext(),task.getException().getMessage(),Toast.LENGTH_LONG).show();
                    }
                });
    }

```


### Send email verification
```java 
      void afterEmailLogin(){

        FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
        user.sendEmailVerification()
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        // email sent
                        Toast.makeText(getContext(),"Email verification send, please verify email",Toast.LENGTH_LONG).show();
                        progressDialog.dismiss();
                        // after email is sent just logout the user and finish this activity
                        FirebaseAuth.getInstance().signOut();
                        Intent home = new Intent(getContext(), SplashActivity.class);
                        startActivity(home);

                    } else {
                        progressDialog.dismiss();
                        Toast.makeText(getContext(),"Email couldn't send, Try again "+task.getException().getMessage(),Toast.LENGTH_LONG).show();
                    }
                });
    }

```

### Check email verification
```java 
          if (FirebaseAuth.getInstance().getCurrentUser() != null){
            if(FirebaseAuth.getInstance().getCurrentUser().isEmailVerified()){
				/// start the app 
			}else{
				/// show some error
			}
		  }

```