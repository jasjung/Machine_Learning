import datetime
import os
import sys

import numpy as np
import pandas as pd
from IPython.display import Audio, display

# so that I do not need to hard code the sound file location
dir_path = os.path.dirname(os.path.realpath(__file__))

path = '/done_sound.mp3'


def done():
    # for jupyter notebook
    display(Audio(filename=dir_path + path, autoplay=True))

    now = datetime.datetime.now()
    print("Finished @", now.strftime("%Y-%m-%d, %H:%M:%S"))


def flat_list(L):
    return [i for sublist in L for i in sublist]


def slack_done(msg='Hello, your program finished running!'):
    os.system("""
        curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"%s\"}' \
        https://hooks.slack.com/services/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
        """ % msg)
    print('sent slack notification')


if __name__ == '__main__':
    done()
    slack_done()
