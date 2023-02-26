---
layout: default
parent: android doc
title: LocationPermission
---

```java 
    private int REQUEST_CODE = 2021;

    public void getLocationPermission() {
        if (!isLocationPermissionGranted(getActivity())) {
            //get location permission
            if (getActivity() != null)
                ActivityCompat          // get permission call
                        .requestPermissions(getActivity(), new String[]{
                                Manifest.permission.ACCESS_FINE_LOCATION,
                                Manifest.permission.ACCESS_COARSE_LOCATION}, REQUEST_CODE);
            //
            //if permission granted
        } else {
            Toast.makeText(getContext(), "Location Permission granted!", Toast.LENGTH_LONG).show();
            dismiss();
        }
    }


    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        if (grantResults.length > 0 &&
                grantResults[0] == PackageManager.PERMISSION_GRANTED &&
                grantResults[1] == PackageManager.PERMISSION_GRANTED &&
                requestCode == REQUEST_CODE)
        {
            onPermissionGrantedListener.isPermissionGranted(true);

        } else {
            onPermissionGrantedListener.isPermissionGranted(false);
        }
        dismiss();
    }

    public static boolean isLocationPermissionGranted(Activity activity) {
        if (activity == null) {
            return false;
        }
        //
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (activity.checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED &&
                    activity.checkSelfPermission(Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED) {
                return true;
            } else {
                return false;
            }
        }
        //
        // always true if bellow version code M
        else {
            return true;
        }
    }



```