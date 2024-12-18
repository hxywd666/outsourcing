import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 邮件配置
smtp_server = 'smtp.126.com'  # 126邮箱的SMTP服务器
smtp_port = 465  # 126邮箱的SMTP端口
sender_email = 'codingfish0706@126.com'  # 发件人邮箱
sender_password = 'FXUCf39ZGWYq9rcV'  # 发件人邮箱密码
receiver_email = 'codingfish0706@126.com'  # 收件人邮箱

# 创建邮件对象
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = '验证码'

# 读取HTML模板
with open('../app/template/email.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 将HTML内容添加到邮件中
msg.attach(MIMEText(html_content, 'html', 'utf-8'))

if __name__ == "__main__":
    # 发送邮件
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")