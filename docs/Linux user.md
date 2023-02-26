---
layout: default
title: Linux user
---
# Linux user
#linux 

# Create new user with home dir
```bash
sudo useradd -m $userName # -m user with home dir
sudo usermod -aG wheel $userName
sudo passwd $userName
```
# Add user to wheel group

## Step 1: Verify the Wheel Group is Enabled
Open the configuration file by entering the command:

```bash
visudo
```

Scroll through the configuration file until you see the following entry:
```bash
## Allows people in group wheel to run all commands
# %wheel        ALL=(ALL)       ALL
```
remove # ( comment ) 

## Step 2: Add User to Group
To add a user to the wheel group, use the command:
```bash
usermod –aG wheel $userName
```

## to list all users :
```bash
cut -d: -f1 /etc/passwd
```

## To remove user :
```bash
sudo userdel username
```

## To remove home directory :
```bash
sudo rm -r /home/username
```

## Login to user
```bash 
  su - username
```
