---
layout: default
parent: android doc
title: Search
---
# Search
### Local Search fragment
```java 
  public class SearchFragment extends Fragment {

    private SearchFragmentBinding binding;
    private RecyclerAdapter adapter;
    private List<ItemValue> itemValues;
    private List<ItemValue> filteredItemValues;


    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        binding = SearchFragmentBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        binding.searchBar.requestFocus();

        itemValues = new ArrayList<>();
        filteredItemValues = new ArrayList<>();
        adapter = new RecyclerAdapter(filteredItemValues);
        binding.recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        binding.recyclerView.setAdapter(adapter);

        itemValues.addAll(fetchData());
        updateList(itemValues);

        binding.searchText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
            }

            @Override
            public void afterTextChanged(Editable s) {
                updateList(filterList(binding.searchText.getText().toString(), itemValues));
            }
        });

    }

    private void updateList(List<ItemValue> newList) {
        filteredItemValues.clear();
        filteredItemValues.addAll(newList);
        if (filteredItemValues.isEmpty()) {
            binding.errorLayout.setVisibility(View.VISIBLE);
        } else {
            binding.errorLayout.setVisibility(View.GONE);
        }
        adapter.notifyDataSetChanged();
    }


    // if the list is bigger please use a background thread
    public List<ItemValue> filterList(String query, List<ItemValue> mainItemList) {
        if (!query.isEmpty()) {
            List<ItemValue> filteredList = new ArrayList<>();
            for (ItemValue i : mainItemList) {
                // filter the way i want, here it check for title and subtitle
                if (i.title.contains(query) || i.subtitle.contains(query)) {
                    filteredList.add(i);
                }
            }
            return filteredList;
        } else {
            return mainItemList;
        }
    }


    private List<ItemValue> fetchData() {
        List<ItemValue> fetch = new ArrayList<>();
        // fetch data....
        return fetch;
    }
    
}


```

### xml
```xml 
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <androidx.cardview.widget.CardView
        android:id="@+id/search_bar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <EditText
            android:id="@+id/search_text"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_margin="5dp"
            android:background="@drawable/search_background"
            android:drawableStart="@drawable/search_icon"
            android:drawablePadding="5dp"
            android:focusable="true"
            android:hint="search something..."
            android:inputType="text"
            android:maxLines="1"
            android:padding="10dp" />
    </androidx.cardview.widget.CardView>

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recycler_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_below="@+id/search_bar" />
    <!--empty layout-->
    <RelativeLayout
        android:id="@+id/error_layout"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_below="@+id/search_bar">

        <ImageView
            android:id="@+id/error"
            android:layout_width="100dp"
            android:layout_height="100dp"
            android:layout_centerInParent="true"
            android:src="@drawable/error_icon" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_below="@+id/error"
            android:layout_centerHorizontal="true"
            android:text="Ops! Nothing to show"
            android:textSize="20dp" />
    </RelativeLayout>
</RelativeLayout>

```