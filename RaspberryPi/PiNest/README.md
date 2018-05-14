# PiNest

(inspired by [nest](https://nest.com))

This is a home security system that you can turn on/off using Amazon Dash. When motion is detected, user will be alerted with either email or text message along with an image of the detected event. 

You will have to configure `motion` on Raspberry Pi to make it save images when motion is detected. There are a lot of parameters to change. Find more about this configuration [here](https://github.com/jasjung/Python/tree/master/RaspberryPi/Webcam).

I used 
[Logitech Webcam](https://www.amazon.com/gp/product/B004FHO5Y6/ref=oh_aui_search_detailpage?ie=UTF8&psc=1), [Raspberry Pi 3](https://www.amazon.com/gp/product/B01LWVVMUI/ref=oh_aui_search_detailpage?ie=UTF8&psc=1) for this project. 

In the future, I want to add a night vision capability. 

## File Description 
- `webcam.py`: When motion is detected, webcam captures the image and saves into, say, `webcam` folder. `webcam.py` continuously for checks for any changes in folder and if there are more files added, meaning motion was detected, it sends that added image to the user. 
- `amazon_dash_for_security_camera_dhcp.py`: A switch to turn on and off the webcam. 

## Video Demonstration 
  - Demo Link: https://youtu.be/vsZC-V8orcY.
  - Initial stage: https://youtu.be/lN0iA-JdOf0
  - Using Amazon Dash as a Camera Switch: (to be uploaded)

