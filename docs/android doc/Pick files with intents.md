
## intent type
```java 
                intent.setType("*/*");
                intent.setType("video/*");
                intent.setType("image/*");

```

## Start intent for file (anyfile)
```java 
                Intent intent = new Intent();
                intent.setType("*/*");
                intent.setAction(Intent.ACTION_GET_CONTENT);
                startActivityForResult(Intent.createChooser(intent, "Select Picture"), PICK_FILE_CODE);

```
