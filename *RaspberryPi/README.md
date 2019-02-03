# Raspberry Pi

All things related to Raspberry Pi. 

## How to set up your raspberry pi for the first time 

https://www.raspberrypi.org/documentation/installation/noobs.md

1. Download zip here: https://www.raspberrypi.org/downloads/ then extract it 
2. Format SD card as FAT (MS-DOS Fat in Mac)
3. Copy the extracted files into the sd card in its root directory. 
4. Insert the SD card into the raspberry pi and follow instructions. 

## General Note 

### Updating  

- sudo apt-get update
- sudo apt-get upgrade

### Install Pandas 

```
sudo apt-get install python3-pandas
```

### VNC (Remote Access)
- sudo apt-get update 
- sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
- sudo raspi-config # to enable vnc -> navigate to Interfacing Options > VNC and select Yes.
- source: https://www.realvnc.com/en/connect/docs/raspberry-pi.html

### PYTHON 
To install python pacakges do: 

- sudo pip install [package_name]


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