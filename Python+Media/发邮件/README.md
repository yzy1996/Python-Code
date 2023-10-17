smtplib 是 SMTP protocol client

**smtplib模块主要负责发送邮件的动作，email模块主要负责构造邮件**




## 提前准备

在邮箱中开启SMTP服务


smtplib.SMTP(smtp_server) as server:
server.starttls()
