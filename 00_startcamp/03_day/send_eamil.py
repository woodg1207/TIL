import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')

email_list = ['wdj1207@naver.com', 'woodk1207@gmail.com', 'woodg1207@gmail.com']
for email in email_list:
    msg = EmailMessage()
    msg['Subject'] = '예습_파이썬으로 메일보내기'
    msg['From'] = 'wdj1207@naver.com'
    msg['To'] = email
    msg.set_content('ㅈㄱㄴ')

    ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
    ssafy.login('wdj1207', password)
    ssafy.send_message(msg)
print('이메일 전송완료')



