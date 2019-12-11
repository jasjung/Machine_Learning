# PlaySound

https://pypi.org/project/playsound/

```
pip install PyObjC

pip install appkit 

pip install playsound 
```

```py
from playsound import playsound
playsound('/path/to/a/sound/file/you/want/to/play.mp3')
```

```
from IPython.display import Audio, display


path = '/payment_success.mp3'

def allDone():
#     display(Audio(url=path, autoplay=True))
    display(Audio(filename=path, autoplay=True))

```