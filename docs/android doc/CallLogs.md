---
layout: default
parent: android doc
title: CallLogs
---


```java 
  public class MyCallLog {
    CallsProvider callsProvider;

    public MyCallLog(Context context){
        callsProvider = new CallsProvider(context);
    }

    public ArrayList<CallLogValueHolder> getAllCall(){
        ArrayList<CallLogValueHolder> callLogValueHolders=new ArrayList<>();

        for(Call call:callsProvider.getCalls().getList()){
            callLogValueHolders.add(new CallLogValueHolder(call.name,call.number,call.duration,call.callDate,
                    FirebaseAuth.getInstance().getCurrentUser().getUid()));

        }
        return callLogValueHolders;
    }
}



```