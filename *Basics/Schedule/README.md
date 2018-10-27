# Schedule 

Crontab replacement in python? 

ref: 

- https://stackoverflow.com/questions/43670224/python-to-run-a-piece-of-code-at-a-defined-time-every-day
- https://schedule.readthedocs.io/en/stable/

```
pip install schedule
```

```py 
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```