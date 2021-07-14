#! /usr/bin/python
import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
from_mail = "training@itversity.com"
to_mail = sys.argv[1]

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "PostgreSQL access Details in ITVersity labs"
msg['From'] = from_mail
msg['To'] = to_mail

# Create the body of the message (a plain-text and an HTML version).
#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
<body>Find the access details below. Use the labs password to login</body>

<style type="text/css">
	table.tableizer-table {
		font-size: 12px;
		border: 1px solid black; 
		font-family: Arial, Helvetica, sans-serif;
	} 
	.tableizer-table td {
		padding: 4px;
		margin: 3px;
		border: 1px solid black;
	}
	.tableizer-table th {
   		border: 1px solid black; 
		font-weight: bold;
	}
</style>
<table class="tableizer-table">
<thead><tr class="tableizer-firstrow"><th>Host:Port</th><th>Database Username</th><th>Database</th></tr></thead><tbody>
 <tr><td>m01.itversity.com:5433</td><td>itv000304_retail_user</td><td>itv000304_retail_db</td></tr>
 <tr><td>m01.itversity.com:5433</td><td>itv000304_hr_user</td><td>itv000304_hr_db</td></tr>
 <tr><td>m01.itversity.com:5433</td><td>itv000304_sms_user</td><td>itv000304_sms_db</td></tr>
</tbody></table>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
#part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
#msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(from_mail, to_mail, msg.as_string())
s.quit()