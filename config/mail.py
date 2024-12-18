from app.utils import read_yaml


mail = read_yaml()['mail']


class MailConfig:
    SMTP_SERVER = mail['host']
    SMTP_PORT = mail['port']
    SMTP_USERNAME = mail['username']
    SMTP_PASSWORD = mail['password']