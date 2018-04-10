# run this py file with sudo in order for scapy to work 
# sudo pip install scapy-python3
# import pcapy 
# from __future__ import print_function

# import matplotlib.pyplot as plt
# sudo python Desktop/Amazon_Dash/amazon_dash3.py

# import packages 
from scapy.all import *
import os 

def arp_display(pkt):
	# raspberry pi 
	if pkt.haslayer(ARP): 
		print('')
		print(pkt[ARP].psrc)
		#if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
		print ("ARP Probe from: " + pkt[ARP].hwsrc)
		
		if pkt[ARP].hwsrc == '[dash info]': # ARP Probe
			print('Pressed LARABAR - start camera')
			# run sudo service motion start 
			os.system('sudo service motion start')

		elif pkt[ARP].hwsrc == '[dash info]': # ARP Probe
			print('Pressed Glad Button - stop camera')
			# run sudo service motion stop 
			os.system('sudo service motion stop')

		else: 
			print('unknown')

print('check1')
print (sniff(prn=arp_display, filter="arp", store=0, count=0))
print('done')