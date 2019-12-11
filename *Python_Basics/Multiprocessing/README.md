# Multiprocessing (+ concurrent.futures, Threading) 

- https://www.youtube.com/watch?v=fKl2JW_qrso
- https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/MultiProcessing
- https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3
- https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/
- https://medium.com/@urban_institute/using-multiprocessing-to-make-python-code-faster-23ea5ef996ba

## Map with argument 

While using `map` if you need to pass in argument, check [this](https://stackoverflow.com/questions/6785226/pass-multiple-parameters-to-concurrent-futures-executor-map) reference. 

```py 
def your_function(your_list, your_argument):
    ...

from itertools import repeat
executor.map(<your_function>, <your_list>, repeat(<'your_argument'>))
```

## Sample Code 


```py
import multiprocessing

start = time.perf_counter()

def do_something(seconds=1):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
```


```py
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
```


```py 
import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
```

