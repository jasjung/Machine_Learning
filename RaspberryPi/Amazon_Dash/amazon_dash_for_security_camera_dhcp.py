# run this py file with sudo in order for scapy to work 
# sudo pip install scapy-python3
# import pcapy 
# from __future__ import print_function

# import matplotlib.pyplot as plt
# sudo python Desktop/Amazon_Dash/amazon_dash3.py

# import packages 
from scapy.all import *
import os 

print('hi')

LARA =  # enter Dash Button's MAC Address here.
GLAD = # enter Dash Button's MAC Address here.

def detect_button(pkt):
	if pkt.haslayer(DHCP) and pkt[Ether].src == LARA:
		print('Pressed LARABAR - start camera')
		# run sudo service motion start 
		os.system('sudo service motion start')

	elif pkt.haslayer(DHCP) and pkt[Ether].src == GLAD:
		print('Pressed Glad Button - stop camera')
		# run sudo service motion stop 
		os.system('sudo service motion stop')
	else: 
		print('else')
		print(pkt.haslayer(DHCP))


print('check1')
sniff(prn=detect_button, filter="(udp and (port 67 or 68))", store=0,count=0)
print('done')