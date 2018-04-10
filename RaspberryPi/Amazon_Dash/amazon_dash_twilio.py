# run this py file with sudo 
# sudo pip install scapy-python3
# easy_install twilio 

# basic tutorial: https://blog.cloudstitch.com/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8

from scapy.all import *

def send_txt():

	from twilio.rest import Client

	client = Client('[enter your info]', '[enter your info]')

	client.messages.create(from_='[enter your info]',
	                       to=('[enter your info]'),
	                       body="[enter your info]")

def arp_display(pkt):
	# regular 
	#if pkt[ARP].op == 1: #who-has (request)
	# raspberry pi 
	if pkt.haslayer(ARP): 
		#if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
		print ("ARP Probe from: " + pkt[ARP].hwsrc)
		if pkt[ARP].hwsrc == '[enter your info]': # ARP Probe
			print('Pressed amazon dash')

			send_txt()

		else: 
			print('unknown')


print (sniff(prn=arp_display, filter="arp", store=0, count=0))

print('done')

