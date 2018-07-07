# -*- coding:utf-8 -*-
import requests
import re
import datetime
import time
import codecs

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


class Email(object):
    def __init__(self):
        self.content = ''
        self.a_url = 'https://github.com/XwLu/Daily-Tips'
        self.time_point = '23:20:00'


    def loadWeb(self):
        html_1 = requests.get(self.a_url)
        html_1.encoding = 'gb2312'
        list1 = re.findall('<p>Start:(.*?):End</p>', html_1.text)
        self.content = ''
        for i in range(len(list1)):
            self.content = self.content + list1[i] + "\n"
            #with codecs.open('/home/luyifan/Project/Email/Tips.txt', 'a', encoding='utf-8') as f:
                #f.write(list1[i]+'\n')

    def sendEmail(self):
        from_addr = '1024507980@qq.com'
        password = 'lyyzdefycyhlbdic'
        to_addr = '416779984@qq.com'
        smtp_server = 'smtp.qq.com'
        msg = MIMEText(self.content, 'plain', 'gb2312')
        msg['From'] = _format_addr(u'虎虎 <%s>' % from_addr)
        msg['To'] = _format_addr(u'陆一帆 <%s>' % to_addr)
        msg['Subject'] = Header(u'来自虎虎的每日计划提示', 'gb2312').encode()
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()


if __name__ == "__main__":
    email = Email()
    print("The email will be sent at" + email.time_point)
    print('Program is Running...')

    while True:
        nowtime = datetime.datetime.now()
        # print(nowtime.strftime('%Y-%m-%d %H:%M:%S'))# 获取年月日时分秒
        time.sleep(1)
        if(nowtime.strftime('%H:%M:%S') == email.time_point):
            #print(nowtime.strftime('%H:%M:%S'))  # 获取时分秒
            email.loadWeb()
            email.sendEmail()

        # email.loadWeb()
        # email.sendEmail()
