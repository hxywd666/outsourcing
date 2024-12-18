import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import MailConfig
from .file import read_email_html


mail = MailConfig()


def login_send_mail(to):
    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = mail.SMTP_USERNAME
    msg['To'] = to
    msg['Subject'] = '登录验证码'

    msg.attach(MIMEText(read_email_html(), 'html', 'utf-8'))

    # 发送邮件
    try:
        with smtplib.SMTP_SSL(mail.SMTP_SERVER, mail.SMTP_PORT) as server:
            server.login(mail.SMTP_USERNAME, mail.SMTP_PASSWORD)
            server.sendmail(mail.SMTP_USERNAME, to, msg.as_string())
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")