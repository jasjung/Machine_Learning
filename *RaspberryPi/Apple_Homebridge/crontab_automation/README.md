# CRON AUTOMATION 

**2020-09**

One issue I had was that every time raspberry pi rebooted for some reason, I had to re-login and spin up homebridge again. This is the solution. 


## Shell 

Create this shell file that checks to see if homebridge is already running, if not, run homebridge. 

```sh
# create a shell file 
touch run_homebridge.sh 

vi run_homebridge.sh
# then copy the following 
```

```sh
if ps -ef | grep -v grep | grep homebridge.sh; then
		echo "already running"
		exit 0 
else 
		echo "running homebridge"
		sh /home/pi/Desktop/run_homebridge.sh
fi 
```


## Cron job 

Create a crontab so that we can check and run the homebridge at a certain time. I assume you know how to edit a file in vim. 

```sh 

# edit your cron job 
crontab -e 

# add the following to run every minute 
*/1 * * * * sh /home/pi/Desktop/run_homebridge.sh > /home/pi/Desktop/homebridge_log.txt
```

