# Homebridge 

TP-LINK Smart Plug does not work with Apple Homekit, but Homebridge bridges that limitation. 

What is Homebridge? [github.com/nfarina/homebridge](https://github.com/nfarina/homebridge)

[TP-Link Smark Plut](https://www.amazon.com/Kasa-Smart-Wi-Fi-Plug-TP-Link/dp/B0178IC734/ref=sr_1_3?s=lamps-light&ie=UTF8&qid=1531027880&sr=1-3&keywords=tp+link+smart+plug)

Referneces: 

- https://www.atpeaz.com/getting-the-tp-link-hs110-smart-plug-to-work-with-apple-home-siri/
- Raspberry-Pi: https://github.com/nfarina/homebridge/wiki/Running-HomeBridge-on-a-Raspberry-Pi
- https://www.imore.com/how-connect-non-homekit-devices-homekit-using-homebridge

### Installing Homebridge to Raspberry Pi 

#### Dependencies 
```sh 
sudo apt-get update
sudo apt-get upgrade

curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Avahi and other Dependencies
sudo apt-get install libavahi-compat-libdnssd-dev
```

#### Main 
```
sudo npm install -g --unsafe-perm homebridge
# sudo npm install -g homebridge

# fixing error 
cd /usr/local/lib/node_modules/homebridge/node_modules/ed25519
sudo node-gyp BUILDTYPE=Release rebuild
```

If you run into errors, try below. 

```
sudo npm -g uninstall homebridge and then npm -g install homebridge --unsafe-perm?
```

Notes: 

```
/usr/lib/node_modules/homebridge/node_modules/ed25519-hap/build
```

## TP-Link Homebridge 
https://www.npmjs.com/package/homebridge-tplink-smarthome

```
sudo npm install -g homebridge-tplink-smarthome
```

## config.json 

config example: https://github.com/nfarina/homebridge/blob/master/config-sample.json

```
~/.homebridge
touch config.json
```

## Other 

### UI

https://www.npmjs.com/package/homebridge-config-ui-x

```
sudo npm install -g --unsafe-perm homebridge-config-ui-x
```

### Camera 

https://appleinsider.com/articles/18/03/21/how-to-create-your-own-homekit-camera-with-a-raspberry-pi-and-homebridge


### Automation switches 

https://www.npmjs.com/package/homebridge-automation-switches
