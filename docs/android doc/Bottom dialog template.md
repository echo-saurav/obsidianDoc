## Bottom dialog template
### Code
```java 
public class CustomBottomSheetDialog extends BottomSheetDialogFragment {
    private CustomBottomsheetDialogBinding binding;
    private String title, subtitle, confirmButton;
    private View.OnClickListener onButtonClickListener;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        binding = CustomBottomsheetDialogBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        binding.title.setText(title);
        binding.subtitle.setText(subtitle);
        binding.confirmButton.setText(confirmButton);
        binding.confirmButton.setOnClickListener(v->{
            dismiss();
            onButtonClickListener.onClick(binding.confirmButton);
        });

    }

    public CustomBottomSheetDialog(String title, String subtitle, String confirmButton, View.OnClickListener onButtonClickListener) {
        this.title = title;
        this.subtitle = subtitle;
        this.confirmButton = confirmButton;
        this.onButtonClickListener = onButtonClickListener;
    }
}

```

### xml
```xml 
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:padding="10dp">

    <TextView
        android:id="@+id/title"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Alert dialog heading"
        android:textSize="20dp"
        android:textStyle="bold" />
    <TextView
        android:id="@+id/subtitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Alert dialog heading" />

    <Button
        android:layout_marginTop="10dp"
        android:id="@+id/confirm_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="confirm"/>
</LinearLayout>
```

