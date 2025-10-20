import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
# Your credentials
sender_email = 'youremail'
app_password = 'your app password'  # go to managae your google account and in  securtiy enable 2fa and search app password and create a temporary password

# Message setup (example)
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = 'sender-email'  # Change this
msg['Subject'] = 'YOU WON 100!!!'
msg.attach(MIMEText(html.substitute(name='Nathan Drake'), 'html'))

# SMTP setup
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()  # Enable TLS
smtp.login(sender_email, app_password)
smtp.send_message(msg)
smtp.quit()

print("Email sent successfully!")
