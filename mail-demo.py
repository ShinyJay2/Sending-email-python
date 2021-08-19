
import os
import smtplib
from email.mime.text import MIMEText


EMAIL_ADDRESS = os.environ.get('EMAIL_ID')
EMAIL_PASSWARD = os.environ.get('EMAIL_PASS')


s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
s.login(EMAIL_ADDRESS, EMAIL_PASSWARD)

msg = MIMEText('메일 내용 테스트')
msg['Subject'] = '메일 보내기 테스트'




s.sendmail(EMAIL_ADDRESS, '07jjh1129@naver.com', msg.as_string())

s.quit()



