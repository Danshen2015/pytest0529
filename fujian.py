#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="testxxx"    #用户名
mail_pass="testxxx2"   #口令 

# 指定sender和rcpt
sender = 'testxxx@163.com'
receivers = ['testxxx@126.com','testxxx@qq.com']   

# 指定信头
message = MIMEMultipart()
message['From'] = ("%s<testxxx@163.com>") % (Header('大神','utf-8'),)
message['To'] = ','.join(receivers)
message.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 指定附件1
att1 = MIMEText(open('2.eml', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="22.eml"'
message.attach(att1)

# 指定附件2
att2 = MIMEText(open('1.eml', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="11.eml"'
message.attach(att2)


msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)

# 指定图片和超链接
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">百度一下</a></p>
<p>图片：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
 
# 指定图片为当前目录
fp = open('20180405100255.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
 
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)



subject = 'Python SMTP 多个附件邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"