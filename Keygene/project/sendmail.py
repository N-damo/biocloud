from . import models
import smtplib
from email.mime.text import MIMEText


def sendmail(email,analysis):
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = ""  # 用户名
    mail_pass = ""  # 密码
    sender = ''  # 发件人邮箱(最好写全, 不然会失败)
    receivers = [email]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    content = '分析任务[{}]已完成，请及时登录网址查看。'.format(analysis)
    title = 'Keygene'  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        message="邮件发送成功"
        update(analysis,message)
    except smtplib.SMTPException as e:
        message="Error: 无法发送邮件 \n{}".format(''.join(e[:50]))
        update(analysis,message)


def update(analysis,message):
    project='_'.join(analysis.split('_')[1:-1])
    username=analysis.split('_')[-1]
    username=models.User.objects.get(name=username)
    user_project=models.User_project_list.objects.get(User=username,name=project)
    user_analysis=models.User_analysis_list.objects.get(User_project_list=user_project,batch=analysis)
    user_analysis.email_send=message
    user_analysis.save()