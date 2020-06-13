#ledfade test lamp setup
#imports
import RPi.GPIO as GPIO
import time

#pre-run cleanup


#setup PI GPIO numbers
GPIO.setmode(GPIO.BCM)



orange = GPIO.PWM(12,100)
brown = GPIO.PWM(16,100)
green = GPIO.PWM(20,100)
yellow = GPIO.PWM(21,100)

