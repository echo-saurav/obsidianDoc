
From Terminal:

```bash
defaults write -g NSWindowShouldDragOnGesture -bool true
```

Once rebooted, you can press `` control+command `` and **left-click** inside _most_ windows and drag to move it.

To stop this behavior, you can delete this `defaults` setting from Terminal:

```bash
defaults delete -g NSWindowShouldDragOnGesture
```









