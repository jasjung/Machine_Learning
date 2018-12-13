# SSH Into Pi on MacOS

Reference: 
[https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md](https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md)


### From Pi 

```
# find host name 
hostname -I # <Your PI IP>

# enable ssh by 
# 1) 
# turn on SSH 
# Enter sudo raspi-config in a terminal window
# Select Interfacing Options
# Navigate to and select SSH
# Choose Yes
# Select Ok
# Choose Finish

# or 
# 2)  
sudo systemctl enable ssh
sudo systemctl start ssh
```

### From Mac 

```
# to ssh into pi from mac 
ssh pi@<Your PI IP>

# to disconnect 
control + d
```

