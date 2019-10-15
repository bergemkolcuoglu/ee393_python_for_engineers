import time
from datetime import datetime
import picamera
import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def sendmail():

    f_time = datetime.now().strftime('%a %d %b @ %H:%M')
    toaddr = 'ugur.dolu@ozu.edu.tr'    # redacted
    me = 'ozupythonproject@gmail.com' # redacted
    msg = MIMEMultipart()
    msg['Subject'] = f_time
    msg['From'] = me
    msg['To'] = toaddr

    fp = open('photo.jpg', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)

    try:
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.starttls()
       s.login("ozupythonproject@gmail.com","EE393py2")
       s.send_message(msg)
       s.quit()
       print("gitti")
    except:
       print ("Error: unable to send email")


