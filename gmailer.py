#!/usr/bin/env python
# 
# Gmailer
"""
Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

    lscianniit@gmail.com
"""

import email.utils
from email.mime.text import MIMEText
from sys import argv
from getpass import getpass

def get_help():
    print('gmailer\nSend an email from a gmail account\nusage:gmailer.py [emailaddress] [subject] [recipient]')

def get_msg():
    msg = input('message:')
    return msg
    
def send_mail(sender, passwd, subjt, recv):
    """
        Send emails with a gmail account 
    """
    user_msg = get_msg()
    
    author = str(sender.split('@')[0]) # strip username from email address to use as author
    #to_addr = []
    #to_addr.append(recv.split(','))
    #print(to_addr)
    
    msg = MIMEText(user_msg)
    msg.set_unixfrom(author)

    #msg['To'] = ', '.join(recv)

    #msg['To'] = email.utils.formataddr(('Recipient', recv))
    msg['From'] = email.utils.formataddr((author, sender))
    msg['Subject'] = subjt
    
    smtp_obj = smtplib.SMTP('smtp.gmail.com')
    
    try:
        smtp_obj.set_debuglevel(True)
        smtp_obj.ehlo()

        if smtp_obj.has_extn('STARTTLS'):       # If server supports starttls initialize TLS
            smtp_obj.starttls()
            smtp_obj.ehlo()
            
        smtp_obj.login(sender, passwd)           # authenticate
        
        for i in recv.split(','):
            msg['To'] = recv
            print("%s\n" % i)
            smtp_obj.send_message(msg, sender, i) # send message to server
        #smtp_obj.sendmail(sender, [recv], msg.as_string())
    finally:
        smtp_obj.quit()
    
if __name__ == '__main__':
    try:
        sender = argv[1]
        passwd = getpass('%s\' password:' % sender)
        subject = argv[2]
        receivers = argv[3]
        
        #to_addr = []
        
        #for addr in receivers.split(','):
        #    to_addr.append(addr)
            
        
    except IndexError:
        get_help()
    try:
        send_mail(sender, passwd, subject, receivers)
    except NameError:
        pass
