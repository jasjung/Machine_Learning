# Amazon Dash

## Resource
- basic tutorial: https://blog.cloudstitch.com/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8
- When you have ARP Layer issue: https://www.tutel.me/c/unix/questions/223255/using+python+and+scapy+to+sniff+for+arp+on+pi

## Notes
- You have to run the python files using sudo. 
- If you are using RaspberryPi, I found that I need to hard wire the RPi and the routher instead of just being connected via wi-fi. Otherwise RPi will not pick up the amazon dash signals. However, you don't need to do that if you are running these codes on regular laptops (mine was being run on Mac). Not too sure why. 

You can use Dash to do whatever you want, such as start security camera, send text, etc. 

Use the `amazon_dash_setup.py` to find out what your dash signal code is. 

## Sending Text Message
- Demo: [coming soon]

## Security Camera 
- Demo: [coming soon]
- I wanted to use dash to turn on and off my security camera system. 
- `amazon_dash_for_security_camera.py`(uses ARP) is my initial attempt to accomplish this task. This worked fine on my Macbook, but once it was used in Raspberry Pi, it did not work reliably. Thus, I used `amazon_dash_for_security_camera_dhcp.py` (uses DHCP), which worked great in pi. 
