# source: https://alexanderle.com/blog/2011/send-sms-python.html

# ATT <number>@mms.att.net
# TMOBILE <number>@tmomail.net
# VERIZON <number>@vtext.net
# ATT <number>@txt.att.net

''' 
issue: you cannot include variable into the message body. For example:

	body = 'hi' 
	server.sendmail( '[your email]', '[your phone number]@mms.att.net', body)

will not work. It has to be
	server.sendmail( '[your email]', '[your phone number]@mms.att.net', 'hi')
'''

# SMTP (simple mail transfer protocol)  
import smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '[your email]', '[email password]' )

# ver1 MMS 
# for some reason, you need to include your email in the first argument, but you don't have to for sms version 
server.sendmail( '[your email]', '[your phone number]@mms.att.net', 'Hello!' )

# ver2 SMS 
server.sendmail( '', '[your phone number]@txt.att.net', 'Hello!' )

print('done')

''' 
import datetime
now = datetime.datetime.now()    
time_stamp = '(Msg Generated at %d/%d %d:%d)' % (now.month, now.day, now.hour, now.minute) 
body  = 'Hello. ' + time_stamp

print(body)
'''