# a way to send text message with image attachment 

# source: https://gist.github.com/alexle/6576366
import smtplib,sys#, base64, sys, re

# python 3 version
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# python 2 version 
'''
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
'''

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '[your info]@gmail.com', '[your info]' )

# input your message here 
msg_text = 'THIEF ALERT'

# add text message
msg = MIMEMultipart()
msg.attach(MIMEText(msg_text, 'plain') )

# add image attachment
fp = open('[your info]', 'rb' )
msg_img = MIMEImage( fp.read() )
fp.close()

msg.attach( msg_img )

#server.sendmail( '', destination, msg.as_string() )
server.sendmail( '[your info]@gmail.com', '[your info]@mms.att.net', msg.as_string())

print('done')