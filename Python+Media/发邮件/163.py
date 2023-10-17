import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


smtp_server = 'smtp.163.com'
smtp_username = '*********'
smtp_password = '*********'

receivers = '*********'

# Set up the email message
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = '*********'
msg["Subject"] = Header('邮件发送测试', 'utf-8')


body = '邮件发送测试'
msg.attach(MIMEText(body, 'plain', 'utf-8'))

try:
    with smtplib.SMTP_SSL(smtp_server) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, receivers, msg.as_string())
        print("发送成功")

except smtplib.SMTPException as e:
    print("无法发送邮", e)