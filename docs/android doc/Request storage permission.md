---
layout: default
parent: android doc
title: Request storage permission
---
# Request storage permission

### pick image
```java 
         //choose image from gallery
        findViewById(R.id.imageView).setOnClickListener(v -> {
            if (isStoragePermissionGranted()) {
                Intent intent = new Intent();
                intent.setType("image/*");
                intent.setAction(Intent.ACTION_GET_CONTENT);
                startActivityForResult(Intent.createChooser(intent, "Select Picture"), PICK_IMAGE_REQ);
            }
        });

```

### after pick image
handle rotation issue [[Programming/Images#Image rotation issue]]
```java 
      @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == PICK_IMAGE_REQ && resultCode == RESULT_OK && data != null && data.getData() != null) {
            Log.d("Edit", "onActivityResult: success");
            Uri imageFileUri = data.getData();
            try {
                this.bitmap = handleSamplingAndRotationBitmap(this, imageFileUri);
                imageView.setImageBitmap(bitmap);
            } catch (Exception e) {
                Toast.makeText(this, "Error selecting image", Toast.LENGTH_LONG).show();
            }
        }
    }

```

### Check for permission
```java 
      public boolean isStoragePermissionGranted() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (checkSelfPermission(Manifest.permission.READ_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED &&
                    checkSelfPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED
            ) {
                return true;
            } else {

                ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.READ_EXTERNAL_STORAGE,
                        Manifest.permission.WRITE_EXTERNAL_STORAGE}, 1);
                return false;
            }
        } else { //permission is automatically granted on sdk<23 upon installation
            return true;
        }
    }


    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED && requestCode == 1) {

            Intent intent = new Intent();
            intent.setType("image/*");
            intent.setAction(Intent.ACTION_GET_CONTENT);
            startActivityForResult(Intent.createChooser(intent, "Select Picture"), PICK_IMAGE_REQ);
            //resume tasks needing this permission
        }

    }

```