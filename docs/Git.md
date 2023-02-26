---
layout: default
title: Git
---
## Other webpage
- [Linux.conf.au 2013- Git For Ages 4 And Up](https://www.youtube.com/watch?v=1ffBJ4sVUb4)
- [git ready » helpful command aliases](https://gitready.com/intermediate/2009/02/06/helpful-command-aliases.html)

# git fixes
- [Git fixes](docs/Git%20fixes.md)

# Git workflow

**while working on code**
- commit after adding every new feature 
- don't work on multiple feature at once 
- add useful commit message 


**While debugging code**
- if something don't work , go back to previous commit when it was working fine (as i have every feature commit) if I want to keep one commit 


## Useful git command
### commit history
```bash
git log 
```

### reset not commited change to last commit
```bash
git checkout $fileName
git checkout $dir
```

### go back to a commit 
```bash
git revert $hash  # <-- get this hash from git log history
```

### List ignored files
```bash
git ls-files . --ignored --exclude-standard --others
```

### List untracked files
```bash
git ls-files . --exclude-standard --others
```

### clone private repo
```bash
git clone https://username@github.com/username/repoName
```

### setup credential
```bash
git config --global credential.helper store
```

### check repo
```bash
git config --get remote.origin.url
```

### Dont show untracked files

```bash
 git config --global status.showUntrackedFiles no 
```

## Reset all untracked change
###   This will unstage all files you might have staged with `git add`:
```bash
git reset
```

###   This will revert all local uncommitted changes (should be executed in repo root):
```bash
git checkout .
```


You can also revert uncommitted changes only to particular file or directory:
```bash
git checkout [some_dir|file.txt]
```

Yet another way to revert all uncommitted changes (longer to type, but works from any subdirectory):   
```bash
git reset --hard HEAD
```

###  This will remove all local untracked files, so _only_ git tracked files remain:
```bash
git clean -fdx
```
  
> **WARNING:** `-x` will also remove all ignored files, including ones specified by `.gitignore`! You may want to use `-n` for preview of files to be deleted.


---

To sum it up: executing commands below is basically equivalent to fresh `git clone` from original source (but it does not re-download anything, so is much faster):

```bash
git reset
git checkout .
git clean -fdx
```

Typical usage for this would be in build scripts, when you must make sure that your tree is absolutely clean - does not have any modifications or locally created object files or build artefacts, and you want to make it work very fast and to not re-clone whole repository every single time.****

## Stop showing untracked files
```bash
$ git config --global status.showUntrackedFiles no
```

For applying this to a single repo, instead use:

```bash
$ git config --local status.showUntrackedFiles no
```

## update submodule
```bash 
git submodule init
git submodule update
```

## Remove sub module
```bash 

git rm --cached path_to_submodule (no trailing slash) as well as
rm -rf path_to_submodule

Then:

Delete the relevant lines from the .gitmodules file. e.g. delete these:
[submodule "path_to_submodule"]
        path = path_to_submodule
        url = https://github.com/path_to_submodule
Delete the relevant section from .git/config. e.g. delete these:
[submodule "path_to_submodule"]
        url = https://github.com/path_to_submodule
rm -rf .git/modules/path_to_submodule
Then, you can finally:

git submodule add https://github.com/path_to_submodule

```

