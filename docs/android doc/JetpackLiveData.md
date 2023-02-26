---
layout: default
parent: android doc
title: JetpackLiveData
---
# JetpackLiveData
## Example
```java 
  public class MainLiveData extends ViewModel {
    private MutableLiveData<List<DetailsManifestValueHolder>> manifestList;
    private MutableLiveData<List<DetailsManifestValueHolder>> todayManifestList;
    private MutableLiveData<Boolean> isChanged;

    public MutableLiveData<List<DetailsManifestValueHolder>> getManifestList() {
        if (manifestList == null) {
            manifestList = new MutableLiveData<>();
        }
        return manifestList;
    }

    public MutableLiveData<List<DetailsManifestValueHolder>> getTodayManifestList() {
        if(todayManifestList==null){
            todayManifestList=new MutableLiveData<>();
        }
        return todayManifestList;
    }

    public MutableLiveData<Boolean> getChanged() {
        if (isChanged == null) {
            isChanged = new MutableLiveData<>();
        }
        return isChanged;
    }

}

```

In the activity
```java 
	MainLiveData mainLiveData = new ViewModelProvider(this).get(MainLiveData.class);
```

in the fragment 
```java 
    MainLiveData mainLiveData = new ViewModelProvider(getActivity()).get(MainLiveData.class);

```
observe data
```java 
   mainLiveData.getManifestList().observe(getViewLifecycleOwner(), this::updateList);

```
```java 
      private void updateList(List<DetailsManifestValueHolder> arrayList) {
	  	////
	  }

```