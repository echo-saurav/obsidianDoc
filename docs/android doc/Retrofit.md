
### Retrofit class
```java 
public class RemoteRepository {
    private static RemoteRepository REMOTE_REPOSITORY;
    private String apiUrl = "https://jsonplaceholder.typicode.com/";
    private Retrofit retrofit;


    public RetrofitTestInterface getInterface() {
        return retrofit.create(RetrofitTestInterface.class);
    }


    public static RemoteRepository getInstance() {
        if (REMOTE_REPOSITORY == null) {
            REMOTE_REPOSITORY = new RemoteRepository();
        }
        return REMOTE_REPOSITORY;
    }

    RemoteRepository() {
        retrofit = new Retrofit.Builder()
                .baseUrl(apiUrl)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
    }

    public interface RetrofitTestInterface {
        @GET("users")
        Call<List<User>> listRepos();
    }
}


```

### Fetch data
```java 
      private void fetchData() {
        ProgressDialog progressDialog = new ProgressDialog(this);
        progressDialog.setTitle("Fetching data");
        progressDialog.setMessage("Please wait, getting user information");
        progressDialog.setCancelable(false);
        progressDialog.show();
        // start fetching data
        Call<List<User>> users = RemoteRepository.getInstance().getInterface().listRepos();
        users.enqueue(new Callback<List<User>>() {
            @Override
            public void onResponse(@NonNull Call<List<User>> call, @NonNull Response<List<User>> response) {
                progressDialog.dismiss();
                if (response.body() == null) {
                    return;
                }
                if (response.code() == 200) {
                    for (User user : response.body()) {
                        binding.text.setText(new StringBuilder(binding.text.getText().toString() + "\n" + user.username + ", location" + user.address.geo.lat));
                    }
                } else {
                    Toast.makeText(MainActivity.this, "Fetching failed", Toast.LENGTH_LONG).show();
                }

            }

            @Override
            public void onFailure(Call<List<User>> call, Throwable t) {
                progressDialog.dismiss();
                Toast.makeText(MainActivity.this, "Fetching failed", Toast.LENGTH_LONG).show();
            }
        });

    }

```