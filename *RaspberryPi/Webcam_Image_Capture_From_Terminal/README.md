# Pi Image Capture from Terminal 

*Public Repo* 

References: 

- [https://www.raspberrypi.org/documentation/usage/webcams/](https://www.raspberrypi.org/documentation/usage/webcams/)
- [https://raspberrypi.stackexchange.com/questions/1714/unable-to-grab-image-from-usb-webcam](https://raspberrypi.stackexchange.com/questions/1714/unable-to-grab-image-from-usb-webcam)
- [https://www.raspberrypi.org/documentation/usage/webcams/](https://www.raspberrypi.org/documentation/usage/webcams/)

## Intall

```
sudo apt-get install fswebcam
fswebcam image.jpg
```

## Demo 

### Capture Image from Terminal (Run from Pi)

```
# -d = device # you do not necessarily have to specify
# -r = resolution 
# you need to wait after you run each command because it takes time for webcam to start and shutdown before the next action. 

fswebcam -d /dev/video0 -r 320x240 test.png
fswebcam -d /dev/video0 -r 640x480 Desktop/test.png
fswebcam -d /dev/video0 -r 1280x720 Desktop/test2.png
fswebcam -r 1280x720 Desktop/test3.png
```

### Copy Image from Pi to Mac (Run from Mac) 

```
scp <Pi User Name>@<Your PI IP>:<Path/To/Your/Image.png> <Directory/To/Your/Desired/Location/>

# might look sth like this 
scp pi@11.1.1.1:Desktop/test.png Desktop/
```