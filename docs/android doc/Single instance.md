---
layout: default
parent: android doc
title: Single instance
---
# Single instance

## Single instance of login info

```java
public class Repository {  
 public static Repository REPOSITORY;  
 private String PREF="APP";  
  
  
 private String login="login";  
  
 public boolean islogedin(Context context){  
	 SharedPreferences sharedPreferences= context.getSharedPreferences(PREF,Context.MODE_PRIVATE);
	 return sharedPreferences.getBoolean(login,false);  
 }  
  
 public void setLoginStatus(Boolean islogedin,Context context){  
	 SharedPreferences sharedPreferences= context.getSharedPreferences(PREF,Context.MODE_PRIVATE);  
	 SharedPreferences.Editor editor=sharedPreferences.edit();
	 editor.putBoolean(login,islogedin);  
	 editor.apply();  
 }  
  
 public static Repository getREPOSITORY() {  
	 if(REPOSITORY==null){  
		 REPOSITORY=new Repository();  
	 }  
	 return REPOSITORY;  
 }  
}

```