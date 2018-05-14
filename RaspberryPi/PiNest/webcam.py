'''
In webcam folder, new images are added when motion is detected. 
This program will scan the folder constantly and send me a text message alert when new file is added, meaning there was motion. 
It will grab the new images and send me the image as well. 

Also, because I do not want too many files to be added with motion, I will delete the images in the folder if there are more than 100 imagaes
'''

print('hi')
path = '/home/pi/webcam'

# EMAIL 
import smtplib
import datetime
import sys 
import os 
import time 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_txt_email(attachment):

	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login( '[your_info]@gmail.com', '[your_info]' )

	# input your message here 
	msg_text = 'THIEF ALERT'

	# add text message
	msg = MIMEMultipart()
	msg.attach(MIMEText(msg_text, 'plain') )

	# add image attachment
	fp = open(path + '/'+ attachment, 'rb' )
	msg_img = MIMEImage( fp.read() )
	fp.close()

	msg.attach( msg_img )

	#server.sendmail( '', destination, msg.as_string() )
	server.sendmail( '[your_info]@gmail.com', '[your_info]@mms.att.net', msg.as_string())


# MAIN 
def main():

	global path 

	temp_len = os.listdir(path)
	# when i delete, i want to delete the first file 
	temp_len.sort()

	print('number of files: %d' % len(temp_len))
	# wait for some time 
	time.sleep(10)

	file_len = os.listdir(path)
	file_len.sort()

	if temp_len != file_len: 
		change = abs(len(temp_len)-len(file_len))

		# a file was added. I want to alert 
		print('%d file was added' % change)
		print('ALERT: motion is detected!')
		
		#print(os.listdir(path)[0])
		# get the name of new files 
		new_imgs = [x for x in file_len if x not in temp_len]
		new_img = new_imgs[int(len(new_imgs)/2)]
		print('new file added: ' + new_img )
		
		send_txt_email(new_img)
		# i dont want to receive too many messages 
		time.sleep(30)
		# EMAIL GOES HERE 

	else: 
		print('everything normal')

	print(os.listdir(path))

	# if there are more than 10 files in the folder, delete the first file. 
	if len(temp_len) > 100:
		print('too many files deleting ' + (temp_len[0]))
		os.remove(path+'/'+temp_len[0])

	print('')	

# run the program 
try:
    while True:
            main()

except KeyboardInterrupt:
	# cntrl + c to interrupt 
    pass

print('done')
