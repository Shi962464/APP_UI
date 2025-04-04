import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


# 邮件内容配置
# 邮件文本

def Email(text):
    msg = MIMEText(text, 'html', 'utf-8')
    # 邮件上显示的发件人
    msg['From'] = formataddr(["Error", 'blooms2464@yeah.net'])
    # 邮件上显示的主题
    msg['Subject'] = "eroor"

    # 发送邮件
    server = smtplib.SMTP_SSL('smtp.yeah.net')
    server.login('blooms2464@yeah.net', 'KOMREKHPADNOKSBF')
    server.sendmail('blooms2464@yeah.net', '2462713107@qq.com', msg.as_string())
    server.quit()