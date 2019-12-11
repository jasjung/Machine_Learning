# Changing Timezone 

Say you are running your code on a server in UTC timezone, but you want to run your code at PST time. 
The code below will help you covert it. 

```py 
# from datetime import timezone, datetime
import pytz
utc_dt = pytz.utc.localize(datetime.utcnow())
pst_tz = pytz.timezone('US/Pacific')
pst_dt = pst_tz.normalize(utc_dt.astimezone(pst_tz))
date_format='%m/%d/%Y %H:%M:%S %Z'
pst_dt.strftime(date_format)

# can also do things like 
pst_dt.hour, pst_dt.minute, pst_dt.second 
``` 

