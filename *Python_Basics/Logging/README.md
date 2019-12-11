# Logging

Reference

- https://stackoverflow.com/questions/8353594/can-python-log-output-without-inforoot
- https://docs.python.org/3/howto/logging.html
- https://stackoverflow.com/questions/9321741/printing-to-screen-and-writing-to-a-file-at-the-same-time
- https://realpython.com/python-logging/


### Simple Version 

```py 
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
    level=logging.INFO)

```

### Output Msg to File and Console

```py
# import logging

logging.basicConfig(level=logging.INFO,
                    format= '%(asctime)s : %(message)s',
                    filename='log.log',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)
logger = logging.getLogger()

logger.info('hello')
```