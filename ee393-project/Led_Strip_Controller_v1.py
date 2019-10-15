import RPi.GPIO as GPIO
import time

RED = 17
GREEN = 22
BLUE = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)

def rgbled(color_R,color_G,color_B): 
        
        if color_R == 1 and color_G == 0 and color_B == 0:
            
            GPIO.output(RED,1)
            GPIO.output(GREEN,0)
            GPIO.output(BLUE,0)
        
        elif color_R == 0 and color_G == 1 and color_B == 0:
            
            GPIO.output(RED,0)
            GPIO.output(GREEN,1)
            GPIO.output(BLUE,0)
         
        elif color_R == 0 and color_G == 0 and color_B == 1:
        
            GPIO.output(RED,0)
            GPIO.output(GREEN,0)
            GPIO.output(BLUE,1)
            
        elif color_R == 1 and color_G == 1 and color_B == 0 :
            
            GPIO.output(RED,1)
            GPIO.output(GREEN,1)
            GPIO.output(BLUE,0)
            
        elif color_R == 1 and color_G == 0 and color_B == 1 :
            
            GPIO.output(RED,1)
            GPIO.output(GREEN,0)
            GPIO.output(BLUE,1)
         
        elif color_R == 0 and color_G == 1 and color_B == 1:
            
            GPIO.output(RED,0)
            GPIO.output(GREEN,1)
            GPIO.output(BLUE,1)
        
        elif color_R == 1 and color_G == 1 and color_B == 1 :
            
            GPIO.output(RED,1)
            GPIO.output(GREEN,1)
            GPIO.output(BLUE,1)
            
        else:
            
            GPIO.output(RED,0)
            GPIO.output(GREEN,0)
            GPIO.output(BLUE,0)    
            
    
def red_blink():
        k = 0
            while k<4 :
               rgbled(1,0,0)
               time.sleep(1)
               rgbled(0,0,0)
               time.sleep(1)
               k=k+1

    
