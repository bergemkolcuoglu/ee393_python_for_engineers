import RPi.GPIO as GPIO
import time
import Led_Strip_Controller_v1
import mail_sending
import terminal_control

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(27,GPIO.IN)
#GPIO.setup(7,GPIO.OUT)

while True:
    i = GPIO.input(27)
    if i == 1:
            i = GPIO.input(27)
            print ("No Detection",i)
            Led_Strip_Controller_v1.rgbled(0,1,0)
            #GPIO.output(7,0)
            #time.sleep(1)
    else:
            i = GPIO.input(27)
            print ("Detected",i)
            Led_Strip_Controller_v1.rgbled(1,0,0)
            terminal_control.takePhoto()
            mail_sending.sendmail()
            Led_Strip_Controller_v1.red_blink()
            

            

            

