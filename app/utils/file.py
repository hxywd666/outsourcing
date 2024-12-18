"""
文件工具包
"""
import yaml
import os


def read_yaml():
    config_path = os.path.join(os.getcwd(), 'application.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def read_email_html():
    html_path = os.path.join(os.getcwd(), 'app', 'template', 'email.html')
    with open(html_path, 'r') as f:
        html_content = f.read()
        return html_content