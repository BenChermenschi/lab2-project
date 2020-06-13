#stepper
import RPi.GPIO as GPIO
import time
#to use raspberry pi gpio number
GPIO.setmode(GPIO.BCM) #GPIO18

#setting up pins for stepper 1
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

#setting up pins for stepper 2
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

print "pin setup complete"

#asigning pins to motors
stepper1 = [24,25,8,7]
stepper2 = [5,6,13,19]
print "pins assigned to motors"

#1 roll cycle
def roll_A(pin1,pin2,pin3,pin4,sleeptime):
	#tick 1
	GPIO.output(pin1,1)
	GPIO.output(pin2,0)
	GPIO.output(pin3,0)
	GPIO.output(pin4,0)
	time.sleep(sleeptime)
	#tick2
	GPIO.output(pin1,0)
	GPIO.output(pin2,1)
	GPIO.output(pin3,0)
	GPIO.output(pin4,0)
	time.sleep(sleeptime)
	#tick3
	GPIO.output(pin1,0)
	GPIO.output(pin2,0)
	GPIO.output(pin3,1)
	GPIO.output(pin4,0)
	time.sleep(sleeptime)
	#tick4
	GPIO.output(pin1,0)
	GPIO.output(pin2,0)
	GPIO.output(pin3,0)
	GPIO.output(pin4,1)
	time.sleep(sleeptime)

def roll_B(pin1,pin2,pin3,pin4,sleeptime):
	#tick 1
	GPIO.output(pin1,0)
	GPIO.output(pin2,0)
	GPIO.output(pin3,0)
	GPIO.output(pin4,1)
	time.sleep(sleeptime)
	#tick 2
	GPIO.output(pin1,0)
	GPIO.output(pin2,0)
	GPIO.output(pin3,1)
	GPIO.output(pin4,0)
	time.sleep(sleeptime)
	#tick 3
	GPIO.output(pin1,0)
	GPIO.output(pin2,1)
	GPIO.output(pin3,0)
	GPIO.output(pin4,0)
	time.sleep(sleeptime)
	#tick 4
	GPIO.output(pin1,1)
	GPIO.output(pin2,0)
	GPIO.output(pin3,0)
	GPIO.output(pin4,0)
	time.sleep(sleeptime)

def stepperRoll_A(stepper,sleeptime):
	GPIO.output(stepper[0],1)
	GPIO.output(stepper[1],0)
	GPIO.output(stepper[2],0)
	GPIO.output(stepper[3],0)
	time.sleep(sleeptime)
	#tick 2
	GPIO.output(stepper[0],0)
	GPIO.output(stepper[1],1)
	GPIO.output(stepper[2],0)
	GPIO.output(stepper[3],0)
	time.sleep(sleeptime)
	#tick 3
	GPIO.output(stepper[0],0)
	GPIO.output(stepper[1],0)
	GPIO.output(stepper[2],1)
	GPIO.output(stepper[3],0)
	time.sleep(sleeptime)
	#tick 4
	GPIO.output(stepper[0],0)
	GPIO.output(stepper[1],0)
	GPIO.output(stepper[2],0)
	GPIO.output(stepper[3],1)
	time.sleep(sleeptime)

def stepperRoll_B(stepper,sleeptime):
	GPIO.output(stepper[0],0)
	GPIO.output(stepper[1],0)
	GPIO.output(stepper[2],0)
	GPIO.output(stepper[3],1)
	time.sleep(sleeptime)
	#tick 2
	GPIO.output(stepper[0],0)
	GPIO.output(stepper[1],0)
	GPIO.output(stepper[2],1)
	GPIO.output(stepper[3],0)
	time.sleep(sleeptime)
	#tick 3
	GPIO.output(stepper[0],0)
	GPIO.output(stepper[1],1)
	GPIO.output(stepper[2],0)
	GPIO.output(stepper[3],0)
	time.sleep(sleeptime)
	#tick 4
	GPIO.output(stepper[0],1)
	GPIO.output(stepper[1],0)
	GPIO.output(stepper[2],0)
	GPIO.output(stepper[3],0)
	time.sleep(sleeptime)

def moveUp(stepper_1,stepper_2,sleeptime):
	stepperRoll_A(stepper_1,sleeptime)
	stepperRoll_B(stepper_2,sleeptime)

def moveDown(stepper_1,stepper_2,sleeptime):
	stepperRoll_A(stepper_2,sleeptime)
	stepperRoll_B(stepper_1,sleeptime)

#main program blink 10 times
print "starting main program"
while 1==1:
	print "iteration"
	moveUp(stepper1,stepper2,0.005)
	
	
	print "iteration end"

print "loop ended"
#cleanup
GPIO.cleanup()
print "program cleaned up"
