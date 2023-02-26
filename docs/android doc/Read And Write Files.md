---
layout: default
parent: android doc
title: Read And Write Files
---
# Read And Write Files
### Get file content
```java 
      @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == PICK_FILE_CODE &&
                resultCode == RESULT_OK &&
                data != null &&
                data.getData() != null) {

            Uri content_describer = data.getData();
            BufferedReader reader = null;
            try {
                // open the user-picked file for reading:
                InputStream in = getContentResolver().openInputStream(content_describer);
                // now read the content:
                reader = new BufferedReader(new InputStreamReader(in));
                String line;
                StringBuilder builder = new StringBuilder();
                while ((line = reader.readLine()) != null){
                    builder.append(line);
                }
                // Do something with the content in
                binding.fileText.setText(builder.toString());
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                if (reader != null) {
                    try {
                        reader.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }

```

### Write file
```java 
  private void writeToFile(String data,Context context) {
    try {
        OutputStreamWriter outputStreamWriter = new OutputStreamWriter(context.openFileOutput("config.txt", Context.MODE_PRIVATE));
        outputStreamWriter.write(data);
        outputStreamWriter.close();
    }
    catch (IOException e) {
        Log.e("Exception", "File write failed: " + e.toString());
    } 
}

```