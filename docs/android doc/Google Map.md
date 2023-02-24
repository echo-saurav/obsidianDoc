### Map fragment
```java 
  public class NewMap extends SupportMapFragment implements OnMapReadyCallback {
    private GoogleMap mMap;
    private List<Marker> markers;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getMapAsync(this);
        markers = new ArrayList<>();
    }

    @Override
    public void onMapReady(@NonNull GoogleMap googleMap) {
        mMap = googleMap;
        // it only decode image resource not xml
        Bitmap img = BitmapFactory.decodeResource(getResources(),R.drawable.bus);
        addNewMarker("Marker in Sydney", new LatLng(-34, 151), img);

        mMap.setOnMapClickListener(latLng -> {
            addNewMarker("Marker in Sydney", latLng, img);
        });
    }

    public void addNewMarker(String title, LatLng latLng, Bitmap bitmap) {

        Marker ms = mMap.addMarker(new MarkerOptions()
                .position(latLng)
                .icon(BitmapDescriptorFactory.fromBitmap(bitmap))
                .title(title));
        markers.add(ms);
//        mMap.moveCamera(CameraUpdateFactory.newLatLng(latLng));
    }

    public void changeMarker(int index, LatLng newpos) {
        Marker m = markers.get(index);
        m.setPosition(newpos);
    }


}


```


### Autocomplete place fragment
```java 
  // Initialize Places.
        Places.initialize(getContext(), getString(R.string.google_maps_key));
        // Initialize the AutocompleteSupportFragment.
        AutocompleteSupportFragment autocompleteFragment = (AutocompleteSupportFragment)
                getChildFragmentManager().findFragmentById(R.id.autoCompleteFragment);

        // Specify the types of place data to return.
        autocompleteFragment.setPlaceFields(Arrays.asList(Place.Field.ID, Place.Field.NAME));

        // Set up a PlaceSelectionListener to handle the response.
        autocompleteFragment.setOnPlaceSelectedListener(new PlaceSelectionListener() {
            @Override
            public void onPlaceSelected(@NonNull Place place) {
                // TODO: Get info about the selected place.
                Log.i(TAG, "Place: " + place.getName() + ", " + place.getId());
            }


            @Override
            public void onError(@NonNull Status status) {
                // TODO: Handle the error.
                Log.i(TAG, "An error occurred: " + status);
            }
        });

```