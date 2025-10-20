import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
# Your credentials
sender_email = 'pksai20044@gmail.com'
app_password = 'becxbwcjlyzkmzyr'  # Replace with the new one

# Message setup (example)
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = 'sailakshman212005@gmail.com'  # Change this
msg['Subject'] = 'YOU WON 100million dollars!!!'
msg.attach(MIMEText(html.substitute(name='Nathan Drake'), 'html'))

# SMTP setup
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()  # Enable TLS
smtp.login(sender_email, app_password)
smtp.send_message(msg)
smtp.quit()

print("Email sent successfully!")