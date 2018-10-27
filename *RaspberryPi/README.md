# RaspberryPi

All things related to Raspberry Pi. 

### SET UP: 
- sudo apt-get update
- sudo apt-get upgrade

### VNC (Remote Access)
- sudo apt-get update 
- sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
- sudo raspi-config # to enable vnc 
- source: https://www.realvnc.com/en/connect/docs/raspberry-pi.html

### PYTHON: 
To install python pacakges do:
- sudo pip install [package_name]

### lock your screen 
- sudo apt-get xscreensaver 

To change setting: 
- xscreensaver

To lock the screen: 
- xscreensaver &
- xscreensaver-command -lock


## Locate 

https://www.howtoforge.com/tutorial/linux-search-files-from-the-terminal/

```
sudo apt-get install locate

locate sunny
locate -c sunny
```

## configuration 

```
sudo raspi-config
```

## vim 

```
sudo apt-get install vim 
```

## Python 3 vs 2 

If you want to specifically install packages to python 3: 

```
sudo apt-get install python3-pip
# for python2 
sudo apt-get install python-matplotlib
# for python3 
sudo apt-get install python3-matplotlib
```