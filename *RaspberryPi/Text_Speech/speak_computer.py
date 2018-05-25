### RASPBERRY PI 
'''
sudo apt-get install espeak
sudo apt-get install espeak python-espeak

source: http://www.instructables.com/id/Make-your-Raspberry-Pi-speak/
source: https://www.dexterindustries.com/howto/make-your-raspberry-pi-speak/

# on command line 
espeak "hello world"
'''

from espeak import espeak
espeak.synth("Hello Instructables!")

### MAC 
from os import system
system('hi owner')	

