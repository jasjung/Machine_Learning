# Google Lighthouse 

https://developers.google.com/web/tools/lighthouse#cli

Taking website screenshot 

```sh 
npm install -g lighthouse
# lighthouse <url>
lighthouse https://google.com 
lighthouse https://google.com --output json --output-path g.json
``` 

Get image 

https://stackoverflow.com/questions/57035531/how-to-get-a-screenshot-and-show-it-to-the-user-after-the-audit-page-speed

```
lighthouseResult.audits['screenshot-thumbnails'].details.items[9].data; 
lighthouseResult.audits['final-screenshot'].details.data;
```
