---
layout: default
parent: android doc
title: Google login
---
# Google login

# Google login
### google login code

```java 
    	// Configure Google Sign In
		private GoogleSignInClient signInClient;
        String token="xoxoxox";
        GoogleSignInOptions gso = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
                .requestIdToken(token)
                .requestEmail()
                .build();
        signInClient = GoogleSignIn.getClient(getContext(), gso);

```


### sign in 

```java 
  
    void googleSignIn() {
		// for not sign in with last account
        if (signInClient != null ) {
            signInClient.signOut();
        }
        String token="xoxoxo";
        GoogleSignInOptions gso = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
                .requestIdToken(token)
                .requestEmail()
                .build();
        signInClient = GoogleSignIn.getClient(getContext(), gso);
        Intent signInIntent = signInClient.getSignInIntent();
        startActivityForResult(signInIntent, RC_SIGN_IN);
    }

```

### activity result

```java 
  
    @Override
    public void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        // Result returned from launching the Intent from GoogleSignInApi.getSignInIntent(...);
        if (requestCode == RC_SIGN_IN) {
            Task<GoogleSignInAccount> task = GoogleSignIn.getSignedInAccountFromIntent(data);
            try {
                // Google Sign In was successful, authenticate with Firebase
                GoogleSignInAccount account = task.getResult(ApiException.class);
                firebaseAuthWithGoogle(account);
            } catch (ApiException e) {
                // Google Sign In failed, update UI appropriately
                Log.w(TAG, "Google sign in failed", e);
            }
        }
    }
```

### with firebase
```java 
  
    private void firebaseAuthWithGoogle(GoogleSignInAccount acct) {
        Log.d(TAG, "firebaseAuthWithGoogle:" + acct.getId());
        progressDialog.show();
        AuthCredential credential = GoogleAuthProvider.getCredential(acct.getIdToken(), null);
        mAuth.signInWithCredential(credential)
                .addOnCompleteListener(getActivity(), task -> {
                    if (task.isSuccessful()) {
                        setProfile(acct.getDisplayName(),acct.getEmail(),acct.getPhotoUrl().toString());
                    } else {
                        progressDialog.dismiss();
                        // If sign in fails, display a message to the user.
                        Log.w(TAG, "signInWithCredential:failure", task.getException());
                        Toast.makeText(getContext(),"Error :"+task.getException().getMessage(),Toast.LENGTH_SHORT).show();
                    }
                });
    }

```