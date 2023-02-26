---
layout: default
parent: android doc
title: CustomDialog
---
## Custom dialog
```java 
  public class CustomDialog extends DialogFragment {
    private String title,subtitle,yes,no;
    private boolean isCancelable;
    private DialogInterface.OnClickListener positiveClickListener,negativeClickListener;

    public CustomDialog(String title, String subtitle,
                        String yes, String no, boolean isCancelable,
                        DialogInterface.OnClickListener positiveClickListener,
                        DialogInterface.OnClickListener negativeClickListener) {
        this.title = title;
        this.subtitle = subtitle;
        this.yes = yes;
        this.no = no;
        this.isCancelable = isCancelable;
        this.positiveClickListener = positiveClickListener;
        this.negativeClickListener = negativeClickListener;
    }


    public CustomDialog(String title, String subtitle,
                        DialogInterface.OnClickListener positiveClickListener) {
        this.title = title;
        this.subtitle = subtitle;
        this.yes = "Yes";
        this.no = "No";
        this.isCancelable = false;
        this.positiveClickListener = positiveClickListener;
    }
    public CustomDialog(String title, String subtitle,boolean isCancelable,
                        DialogInterface.OnClickListener positiveClickListener) {
        this.title = title;
        this.subtitle = subtitle;
        this.yes = "Yes";
        this.no = "No";
        this.isCancelable = isCancelable;
        this.positiveClickListener = positiveClickListener;
    }


    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        // Use the Builder class for convenient dialog construction
        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        builder.setMessage(subtitle).setTitle(title)
                .setCancelable(isCancelable)
                .setPositiveButton(yes, positiveClickListener);

        if(negativeClickListener!=null){
            builder.setNegativeButton(no,negativeClickListener);
        }
        // Create the AlertDialog object and return it
        return builder.create();
    }
}

```

