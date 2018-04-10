''' 
A way to apply CSS styling to your email. 
This was designed to style pandas dataframe. 
'''


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "x@x.com"
you = ['x@x.com']

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "_"
msg['From'] = me
msg['To'] = ', '.join( you )

html = """\
<html>

	<style>
		table { 
		    color: #333;
		    font-family: Helvetica, Arial, sans-serif;
		    /*width: 640px;*/
		    width: 100%;
		    border-collapse: collapse; 
		    border-spacing: 1;
		}
		 
		td, th { 
		    border: 1px solid #CCC; /*transparent;*/ /* No more visible border */
		    height: 30px;
		    transition: all 0.3s;  /* Simple transition for hover effect */
		}
		 
		th { 
		    background: #00BF45;  /* Darken header a bit */
		    font-weight: bold;
			text-align: center;

		}
		 
		td { 
		    /*background: #FAFAFA;*/
		    text-align: center;
		}
		h1 { text-decoration: underline;}

		tr:nth-child(even) {background: #D8D8D8} /* */ 

		tr:nth-child(odd) {background: #F1F1F1} /* DFDFDF EBEBEB*/ 


		/* Cells in even rows (2,4,6...) are one color */       

		/* tr:nth-child(even) td { background: #F1F1F1; } */  
		 
		/* Cells in odd rows (1,3,5...) are another (excludes header cells)  */       

		/* tr:nth-child(odd) td { background: #FEFEFE; } */ 
		 
		tr td:hover { background: #DC9600; color: #FFF; } /*#666*/
		tr th:hover { background: #DC9600; color: #FFF; } /*#666*/
		
		/* Hover cell effect! */

	</style>
 

  <head></head>
  <body>
    <p style="font-size:20px" > This is an automated alert for Panoptes Project.<br>
    </p>
  </body>
</html>
"""


html += '<p style="font-size:20px" > '
html += ' '
html += '</p>'

html += '<p style="font-size:20px"> <u>'
html += ' '
html +='</u></p>'

html += XXX.to_html(index=False)

html += '<br>'
html += '<p style="font-size:20px"> <u>'
html += ' '
html +='</u></p>'
html += XXX.to_html(index=False, escape=False)

html += '<br>'
html += '<p style="font-size:20px"> <u>'
html += ' '
html +='</u></p>'
html += XXX.to_html(index=False, escape=False)


# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
#msg.attach(part1)
msg.attach(MIMEText(html, 'html'))


print(msg)

# Send the message via local SMTP server.
#s = smtplib.SMTP('localhost')
RELAY_SERVER = " "
s = smtplib.SMTP(RELAY_SERVER)

# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()

print('done')




