##!/bin/bash

# copy new files
echo "copy new files"
rm -rf docs
mkdir docs    
cp -R ~/media/obsidian/Eternal/docs/*  docs/

# push to github
echo "push to gitub"
git add .
git commit -m "$(date)" 
git push -u origin main


## This is for pm2 
## It needs to be keep running
## It will restart by pm2 cronjob
exit_code=$?

if [ $exit_code -eq 0 ]; then
  echo "success"
  while true; do
    sleep 1000
  done
else
  echo "error"
  exit $exit_code
fi

