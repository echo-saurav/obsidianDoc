

## Rcyclerview template
### Adapter
```java 
  public class RecyclerAdapter extends RecyclerView.Adapter<ImageItem> {
    private List<ItemValue> itemValues;

    public RecyclerAdapter(List<ItemValue> itemValues) {
        this.itemValues = itemValues;
    }

    @NonNull
    @Override
    public ImageItem onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new ImageItem(ImageItemBinding.inflate(LayoutInflater.from(parent.getContext()), parent, false));
    }

    @Override
    public void onBindViewHolder(@NonNull ImageItem holder, int position) {
        holder.setValues(itemValues.get(position));
    }

    @Override
    public int getItemCount() {
        return itemValues.size();
    }
}

```

### Itemview
```java 
public class ImageItem extends RecyclerView.ViewHolder {
    private ImageItemBinding binding;

    public ImageItem(ImageItemBinding imageItemBinding) {
        super(imageItemBinding.getRoot());
        this.binding = imageItemBinding;
    }

    public void setValues(ItemValue value) {
        binding.title.setText(value.title);
        binding.subtitle.setText(value.subtitle);
        Picasso.get().load(value.imageUrl).into(binding.imageView);
        binding.getRoot().setOnClickListener(view -> {
            ((MainActivity) view.getContext()).replaceFragment(new PostDetailsFragment());
        });
    }
}


```

Recycler view layout
```java 
        binding.recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        binding.recyclerView.setLayoutManager(new StaggeredGridLayoutManager(2, StaggeredGridLayoutManager.VERTICAL));
        binding.recyclerView.setLayoutManager(new GridLayoutManager(getContext(),2));

```