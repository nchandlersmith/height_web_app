import smtplib
from email.mime.text import MIMEText

def send_email(email_address, height):
    from_email = ''
    from_password = ''
    to_email = email_address

    subject = 'Height Data'
    body = 'Hi there, your height is <strong> {0}</strong>.'.format(height)
    message = MIMEText(body, 'html')
    message['Subject'] = subject
    message['To'] = to_email
    message['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(message)