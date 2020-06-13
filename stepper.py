#stepper
import RPi.GPIO as GPIO
import time
#to use raspberry pi gpio number
GPIO.setmode(GPIO.BCM) #GPIO18

#setting up pins
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
print "pin setup complete"


#1 roll cycle
def roll(tijd):
	print "time is"
	print tijd
	#tick 1
	GPIO.output(24,1)
	GPIO.output(25,0)
	GPIO.output(8,0)
	GPIO.output(7,0)
	time.sleep(tijd)
	print "tick 1 end"
	#tick2
	GPIO.output(24,0)
	GPIO.output(25,1)
	GPIO.output(8,0)
	GPIO.output(7,0)
	time.sleep(tijd)
	print "tick 2 end"
	#tick3
	GPIO.output(24,0)
	GPIO.output(25,0)
	GPIO.output(8,1)
	GPIO.output(7,0)
	time.sleep(tijd)
	print "tick 3 end"
	#tick4
	GPIO.output(24,0)
	GPIO.output(25,0)
	GPIO.output(8,0)
	GPIO.output(7,1)
	time.sleep(tijd)
	print "tick 4 end"

#main program blink 10 times
print "starting main program"
while 1==1:
	print "iteration"
	
	roll(0.005)
	print "iteration end"

print "loop ended"
#cleanup
GPIO.cleanup()
print "program cleaned up"
