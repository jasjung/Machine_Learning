from playsound import playsound
import os
import datetime

# so that I do not need to hard code the sound file location
dir_path = os.path.dirname(os.path.realpath(__file__))

def done():
    playsound(dir_path + '/your_music_file.m4a')
    now = datetime.datetime.now()
    print ("Finished @", now.strftime("%Y-%m-%d, %H:%M:%S"))

done()
