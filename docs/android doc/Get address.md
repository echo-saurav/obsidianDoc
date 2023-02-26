---
layout: default
parent: android doc
title: Get address
---
# Get address


```java 
      String getAddress(double latitude,double longitude){
        Geocoder geocoder;
        List<Address> addresses;
        geocoder = new Geocoder(this, Locale.getDefault());


        try {
            addresses = geocoder.getFromLocation(latitude, longitude, 1); // Here 1 represent max location result to returned, by documents it recommended 1 to 5
            if(addresses.isEmpty()){
                return "unknown address latitude: "+latitude+"lon: "+longitude;
            }
            String address = addresses.get(0).getAddressLine(0); // If any additional address line present than only, check with max available address lines by getMaxAddressLineIndex()
            String knownName = addresses.get(0).getFeatureName(); // Only if available else return NULL

          return address+"\n"+knownName;


        } catch (IOException e) {
            e.printStackTrace();
        }
        return "unknown address latitude: "+latitude+"lon: "+longitude;

    }

```