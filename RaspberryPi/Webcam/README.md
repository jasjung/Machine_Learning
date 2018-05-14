# Webcam

- raspi-config 
  -   disable camera 
- sudo apt-get install fswebcam
- fswebcam -r 640x480 --no-banner image3.jpg 
(need to do the above commands for motion to work for some reason)

- sudo apt-get install motion 
- sudo nano /etc/motion/motion.conf
  -   DAEMON = OFF (change to ON)
  -   Webcam_localhost = ON (Change to OFF)
  -   stream_localhost ON (Change to OFF)
  -   output_pictures ON (Change to OFF) 
  -   ffmpeg_output_movies ON (Change to OFF) 
  -   framerate 2 (Change to 10) # smoother video 
  -   stream_maxrate 1 (Change to 10) # more real time 
  -   threshold: change to higher value if you want motion detection to be less sensitive. 

- If you want to start saving photos 
  -   target_dir (some absolute location eg. /home/pi/webcam)
  -   sudo chmod 77 /home/pi/webcam # this is necessary. 
  
- sudo nano /etc/default/motion
  -   start_motion_daemon = no (change to yes)
  
- sudo service motion start

- ifconfig # to find your local IP Address 
- Finally, type your [IP ADDRESS]:[PORT] on your web browser. eg. "192.168.1.103:8081"
- sudo service motion stop

- sudo apt-get purge motion # to remove motion 
- source: 
  - https://raspberrypi.stackexchange.com/questions/45680/failed-to-open-video-device-dev-video0-no-such-file-or-directory-with-normal
  - https://pimylifeup.com/raspberry-pi-webcam-server/

- There are many tutorials how you can access this webcam over the internet directly. However, if you have VNC set up, you can just have the brower up on the raspberry pi and simply your pi via VNC. I find this way much simpler. 
