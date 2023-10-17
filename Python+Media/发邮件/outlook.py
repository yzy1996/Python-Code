import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from email.header import Header


# Set up the SMTP server
smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_username = '*********'
smtp_password = '*********'

receivers = '*********'

# Set up the email message
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = receivers
msg["Subject"] = Header('Python自动发送的邮件','utf-8')


with open('content.txt', 'r', encoding='utf-8') as f:
    body = f.read()
msg.attach(MIMEText(body, 'html', 'utf-8'))

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, receivers, msg.as_string())
        print("发送成功") 

except smtplib.SMTPException as e:
    print("无法发送邮", e)