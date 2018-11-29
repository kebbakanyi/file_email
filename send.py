from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import smtplib
import credentials
import datetime

# get credentials from the credentials.py file
from_addr = credentials.EMAIL_ADDRESS
to_addr = credentials.TO_ADDRESS

msg = MIMEMultipart()

# Add the to and from email address and the subject.
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = f"Log files for {datetime.datetime.today().strftime('%Y-%m-%d')}"

# write body of the email
body = f"This is the Log files for {datetime.datetime.today().strftime('%Y-%m-%d')}"

msg.attach(MIMEText(body, 'plain'))

# add the filename
filename = "AWS_Test.csv"
# add file path
attachment = open("/Users/kebba/Desktop/AWS_Test.csv", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

# send email`
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_addr, credentials.PASSWORD)
text = msg.as_string()
server.sendmail(from_addr, to_addr, text)
server.quit()
