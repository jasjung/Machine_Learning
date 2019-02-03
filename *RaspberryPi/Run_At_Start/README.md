# Run at Start

- https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up
- https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/

I could not get my webcam to NOT START when my raspberry pi restarts. So I thought I should run `sudo service motion stop` command at reboot. 

The following method did not work! But I am leaving it for my future reference. 

```
sudo nano /etc/rc.local

# inside rc.local file 
sudo service motion stop &  > /home/pi/Desktop/log_motion.txt 2>&1
exit 0

# to check
sudo reboot
```


```
sudo vi /etc/default/motion
```