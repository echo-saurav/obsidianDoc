---
layout: default
parent: android doc
title: ProfileFragment
---
# ProfileFragment

```java 
  public class ProfileFragment extends Fragment {

    private ProfileLayoutBinding binding;
    private String imageUrl, heading, subtitle;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        binding = ProfileLayoutBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        if (getArguments() != null) {
            imageUrl = getArguments().getString("image") != null ? getArguments().getString("image") : "";
            heading = getArguments().getString("heading") != null ? getArguments().getString("heading") : "";
            subtitle = getArguments().getString("subtitle") != null ? getArguments().getString("subtitle") : "";
            setValues();
        }
    }
    private void setValues() {
        binding.title.setText(heading);
        binding.subtitle.setText(subtitle);
        Picasso.get().load(imageUrl).into(binding.imageView);
    }
}


```