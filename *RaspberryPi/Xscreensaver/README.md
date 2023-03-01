# Lock Screen - Xscreensaver

### lock your screen 
- `sudo apt-get install xscreensaver`

To change setting: `xscreensaver`

To lock the screen: 

- `xscreensaver &`
- `xscreensaver-command -lock`

### lock shortcut 

```sh 
echo "alias lock=\"xscreensaver-command -lock\"" >> .bashrc
```

Then simply type `lock` in terminal to lock screen 
