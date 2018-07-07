# -*- coding: utf-8 -*-

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
        self.sendEmail('Test！')

    def sendEmail(self, content):
        from_addr = '1024507980@qq.com'
        password = 'lyyzdefycyhlbdic'
        to_addr = 'luyifan1995@sjtu.edu.cn'
        smtp_server = 'smtp.qq.com'
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = _format_addr(u'虎虎 <%s>' % from_addr)
        msg['To'] = _format_addr(u'陆一帆 <%s>' % to_addr)
        msg['Subject'] = Header(u'来自虎虎的每日计划提示', 'utf-8').encode()
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()


if __name__ == "__main__":
    Email()




