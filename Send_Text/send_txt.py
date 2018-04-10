# easy_install twilio 

from scapy.all import *

def send_txt():

	from twilio.rest import Client

	client = Client('[enter your info]', '[enter your info]')

	client.messages.create(from_='[enter your info]',
	                       to=('[enter your info]'),
	                       body="[enter your info]")

send_txt()