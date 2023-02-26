---
layout: default
parent: android doc
title: ActivityAndNavigation
---
### Call intent
```java 
              Intent callIntent = new Intent(Intent.ACTION_CALL);
            callIntent.setData(Uri.parse("tel:" + phoneNumber));
            startActivity(callIntent);

```

