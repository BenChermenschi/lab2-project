#ldr
#imports
import RPi.GPIO as GPIO
import time
#clearing any previous uses
GPIO.cleanup()

#setting up raspberry GPIO numbers
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN) #GPIO 17 is input
GPIO.setup(27,GPIO.IN)
GPIO.setup(18,GPIO.OUT) #GPIO 18 is output

#loop forever or ctrl^C

while 1==1:
	if (GPIO.input(17)==1) or GPIO.input(27): #input low active
		print "licht aan"
		print "klep down"
		time.sleep(0.3) #anti-bouncing
	else:
		print "licht uit"
		print "klep up"
		time.sleep(0.3) #anti-bouncing

GPIO.cleanup()
