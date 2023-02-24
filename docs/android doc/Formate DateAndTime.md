```java 
  		Date date = Calendar.getInstance().getTime();
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("y-MM-dd", Locale.US);
        String deliveryDate = simpleDateFormat.format(date);

```