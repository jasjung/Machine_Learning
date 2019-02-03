# Webcam


### Install 

```
sudo apt-get install fswebcam
sudo apt-get install motion
```

## fswebcam

```
- raspi-config 
  -   disable camera 
```

- `sudo apt-get install fswebcam`
- `fswebcam -r 640x480 --no-banner image3.jpg` 
(need to do the above commands for motion to work for some reason)

## Motion 

### Motion Config 

```
sudo nano /etc/motion/motion.conf
```

-  **DAEMON** = OFF (change to ON) -> actually, don't unless you want the camera to start when you start up the machine.
-  **webcam_localhost**: OFF 
-  **stream_localhost**: OFF
-  **ffmpeg_output_movies**: ON (Change to OFF) 
-  **stream_maxrate**: 1 (Change to 10) # more real time 
-  **threshold**: 1500 (Change to **15,000**) - change to higher value if you want motion detection to be less sensitive. 
-  **framerate**: 2 (Change to **10**) # smoother video 
-  **Width and Height**: **1280 x 720** pixels
- Image File Output 
 - **quality**: 75 -> 100
- FFMPEG Options 
- If you want to start saving photos 
  -   **target_dir** (some absolute location eg. /home/pi/webcam)
  -   `sudo chmod 777 /home/pi/webcam` # this is necessary 
  -   **output_pictures**: ON 
  -   **picture_filename**: `%Y-%m-%d:%H%M%S-%q` (I prefer this format) 

### Default Motion

```
sudo nano /etc/default/motion
```

- **start\_motion_daemon**: YES 
 - You need this to be YES if you want `sudo service motion start` to work (). However this created issue when I reboot, the motion starts automatically, but I did not want this behavior. Therefore, alternative is explaiend . But this didn't work either. 
 - This method is same as the method described below. [reference](https://www.raspberrypi.org/forums/viewtopic.php?t=49565)
 
```
sudo nano /etc/init.d/motion

Find line: DEFAULTS=/etc/default/$NAME
Replace with #DEFAULTS=/etc/default/$NAME

sudo systemctl daemon-reload
```

### rc.local 

To turn off motion on reboot 

```
sudo nano /etc/rc.local

# add the following before exit 0 
sudo service motion stop &
```

### Start

`sudo service motion start` or `sudo service motion stop`


### Webcam Streaming

```
ifconfig # to find your local IP Address 

Finally, type your [IP ADDRESS]:[PORT] on your web browser. eg. "192.168.1.103:8081"
```

### Remove 

- source: 
  - https://raspberrypi.stackexchange.com/questions/45680/failed-to-open-video-device-dev-video0-no-such-file-or-directory-with-normal
  - https://pimylifeup.com/raspberry-pi-webcam-server/

```
sudo apt-get purge motion # to remove motion 
```

## ETC 

`sudo systemctl enable motion`

There are many tutorials how you can access this webcam over the internet directly. However, if you have VNC set up, you can just have the brower up on the raspberry pi and simply your pi via VNC. I find this way much simpler. 
