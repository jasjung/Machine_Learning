# pip install Client
# easy_install twillo  

# import packages 
import requests 
from bs4 import BeautifulSoup
import time
import datetime
from tqdm import trange

def fetch_price():
    url = 'http://www.bing.com/search?q=bitcoin+price'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find_all('div','b_hide')
    return float(table[0].find(text=True))

def send_txt(body):
	from twilio.rest import Client

	client = Client('[your info here]', '[your info here]')

	client.messages.create(from_='[[your info here] info here]',
	                       to=('6503034928'),
	                       body=body)


counter = 0
SET = 0

def main():

    global counter 
    global SET 

    now = datetime.datetime.now()    

#    if now.hour > 7 and now.hour < 24: 

    CUR = fetch_price() 

    # if this is our first time running the script 
    if counter == 0: 
        SET = CUR

    if counter == 24: 
        SET = CUR
        counter = 1 

    # global SET 
    # get current price 
    
    print('CUR ' + str(CUR))
    print('SET ' + str(SET))

    percent_change = (CUR-SET)/SET*100

    print('percent change ' + str(percent_change))
    
    # if there is 1% change 
    if abs(percent_change) > 1:
        # if above 
        if CUR > SET: 
            print('above')
            # send alert        	 
            body = 'hey GOOD news. bitcoin is now %d from %d.' % (CUR,SET)
            body += ' %s%% change.' % (str(round(percent_change,1)))
            send_txt(body)
            print(body)

        # if below 
        elif CUR < SET: 
            print('below')
            # send alert 
            body = 'hey BAD news. bitcoin is now %d from %d.' % (CUR, SET)
            body += ' %s%% change.' % (str(round(percent_change,1)))

            print(body)
            send_txt(body)

        else:
        	print('else clause')
            #body = 'error'
            #send_txt(body)
    	# reset the price 

        SET = CUR 

        print('now new set price is %d' % SET)
    # wait for 1 hour: 60 seconds x 60 

    print('now wait a bit...')

    for i in trange(3600):
        time.sleep(1)    
    #time.sleep(3600)

    counter +=1


# run the program 
try:
    while True:
            main()
except KeyboardInterrupt:
	# cntrl + c to interrupt 
    pass






