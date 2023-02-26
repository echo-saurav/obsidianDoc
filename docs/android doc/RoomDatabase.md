---
layout: default
parent: android doc
title: RoomDatabase
---
# RoomDatabase
### Pojo class
```java 
@Entity
public class Task {
    @NonNull
    @PrimaryKey(autoGenerate = true)
    public int id;
    @ColumnInfo
    public boolean isChecked;
    @ColumnInfo
    public String text;
    @ColumnInfo
    public String subtext;

    public Task() {
    }

    public Task( boolean isChecked, String text, String subtext) {
        this.isChecked = isChecked;
        this.text = text;
        this.subtext = subtext;
    }
}


```

### Interface 
```java 
@Dao
public interface TaskDao {

    @Query("SELECT * FROM task")
    List<Task> getAllTasks();

    @Query("SELECT * FROM task WHERE isChecked=1")
    List<Task> getDoneTasks();

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    void addNewTask(Task task);
    @Update(onConflict = OnConflictStrategy.REPLACE)
    void updateProduct(Task task);


    @Delete
    void deleteTask(Task task);

}


```

### Database
```java 
  @Database(entities = {Task.class},version = 2)
public abstract class TaskDatabase extends RoomDatabase {
    public abstract TaskDao taskDao();
}


```

### Single instance for database
```java 
  public class LocalRepo {
    private static LocalRepo localRepo;


    public LocalRepo( ) {
    }

    public TaskDatabase getDatabase(Context context){
        return Room.databaseBuilder(context,
                TaskDatabase.class, "task")
                .allowMainThreadQueries() // task fetch in foreground (not recomended)
                .fallbackToDestructiveMigration() // changing version without error
                .build();
    }

    public static LocalRepo getLocalDatabaseInstance(){
        if (localRepo ==null){
            return new LocalRepo();
        }
        return localRepo;
    }

}


```

### fetching data
```java 
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

```