import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromemail= os.getenv('FROM_EMAIL')

def send_email(to_mail, username):
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "PostgreSQL access Details in ITVersity labs"
	msg['From'] = fromemail
	msg['To'] = to_mail
	html = f"""
	<html>
	<head></head>
	<body>Find the access details below. Use the labs password to login</body>
	
	<style type="text/css">
	table.tableizer-table {
		"font-size": 12px;
		border: 1px solid black; 
		font-family: Arial, Helvetica, sans-serif;
	} 
	.tableizer-table td {
		"padding": 4px;
		margin: 3px;
		border: 1px solid black;
	}
	.tableizer-table th {
		"border": 1px solid black; 
		font-weight: bold;
	}
	</style>
	<table class="tableizer-table">
	<thead><tr class="tableizer-firstrow"><th>Host:Port</th><th>Database Username</th><th>Database</th></tr></thead><tbody>
	<tr><td>m01.itversity.com:5433</td><td>{username}_retail_user</td><td>{username}_retail_db</td></tr>
	<tr><td>m01.itversity.com:5433</td><td>{username}_hr_user</td><td>{username}_hr_db</td></tr>
	<tr><td>m01.itversity.com:5433</td><td>{username}_sms_user</td><td>{username}_sms_db</td></tr>
	</tbody></table>
	</html>
	"""

	part1 = MIMEText(html, 'html')
	msg.attach(part1)

	# Send the message via local SMTP server.
	s = smtplib.SMTP('localhost')
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(fromemail, to_mail, msg.as_string())
	s.quit()
