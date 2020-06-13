#full code As written by Ben Chermenschi 2020 - ****

#imports
import RPi.GPIO as GPIO
import time
from datetime import datetime
print("import - complete")

print("preparing for logging")
now = datetime.now()
current_time = now.strftime("%d-%m-%Y_%H:%M:%S")
print ("Current time is ", current_time)

filename = "log-fullcode-" + current_time + ".txt"
file_object = open(filename,"w+")

#logging modules
def logwrite(text):
	now = datetime.now()
	current_time = now.strftime("%d-%m-%Y_%H:%M:%S")
	
	output = output = current_time+ " " + text + " \r\n"
	file_object.write(output)
	print(output)

logwrite("done")

#setting GPIO mode to pin numbers
GPIO.setmode(GPIO.BCM)
logwrite("GPIO mode set - BCM")


#setting required pins
logwrite('setting pins 0/4')
#pins for stepper 1
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
logwrite("setting pins 1/4 - stepper 1 complete")

#pins for stepper 2
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
logwrite("setting pins 2/4 - stepper 2 complete")

#pins for LDR
GPIO.setup(17,GPIO.IN) #GPIO 17 is input
GPIO.setup(27,GPIO.IN)
GPIO.setup(18,GPIO.OUT) #GPIO 18 is output
logwrite("setting pins 3/4 - LDR complete")

#pins for led light
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
logwrite("setting pins 4/4 - led fader complete")
logwrite("pin setup - Complete")

#declaration of variables
logwrite("dec vars 0/5")

#speed/waittime vars 
time_ledfade = 0.2
time_steppers = 0.01
logwrite("dec vars 1/5 - speed set")

#status tracker

hatchStatus = False #True means hatch is up, False means hatch is Down
hatchMove = True #means that hatch has already moved, False means hatch hasn't already moved

previousSunshine= False #checks what the value of the previous check was
sunshine= False #means that sun is shining, False means its "dark"

isLightOn= False
hasLightStarted= False #checks if the lightfade has run its start sequence

logwrite("dec vars 2/5 - status trackers setup")

#assigning pins to motors
stepper1 = [24,25,8,7]
stepper2 = [5,6,13,19]
logwrite("dec vars 3/5 - pins assigned to motors")

#assigning pins to wire colors for better control of ledfade
orange = GPIO.PWM(12,1)
brown = GPIO.PWM(16,1)
green = GPIO.PWM(20,1)
yellow = GPIO.PWM(21,1)
logwrite("dec vars 4/5 - ledfade vars setup")

#stepper cycle control 
stepperTicksForCycle = 130
logwrite("dec vars 5/5 - stepper control established")
logwrite("dec vars - Complete")

#Functions to make program modular
logwrite("setting up functions")



#general modules
def sunRise():
	#if hatch hasn't moved and hatch is down
	if	hatchMove==False and hatchStatus==False:
		global hatchMove
		global hatchStatus
		logwrite("moving the hatch from down to up")
		StepperCycleUp(stepper1,stepper2,time_steppers,stepperTicksForCycle)
		hatchMove=True
		hatchStatus=True
		if isLightOn==False:
			logwrite("Light is off, initiating ledfade to on")
			ledfade_startup()
			ledfade_on()
		logwrite("adding hatchlock from sunrise")
		
	
def sunSet():
	#if hatch hasn't moved and hatch is up
	if hatchMove==False and hatchStatus==True:
		global hatchMove
		global hatchStatus
		print("moving the hatch from up to down")
		StepperCycleDown(stepper1,stepper2,time_steppers,stepperTicksForCycle)
		hatchMove=True
		hatchStatus=False
		if isLightOn==True:
			logwrite("Light is on, initiating ledfade to out")
			ledfade_out()
			ledfade_stop()
			
		
		print("adding hatchlock from sunset")

def checklightChange():
	#if there is a lock on the hatch and the light has changed, remove the lock
	if hatchMove==True and sunshine!=previousSunshine:
		logwrite("removing hatch lock")
		#telling python to use the global variables instead of defining new ones
		global hatchMove
		global previousSunshine
		global sunshine
		hatchMoveSTR = str(hatchMove)
		line = "hatchmove = " + hatchMoveSTR
		logwrite(line)
		hatchMove= False
		hatchMoveSTR = str(hatchMove)
		line = "hatchmove = " + hatchMoveSTR
		logwrite(line)
	
	previousSunshine=sunshine

#stepper modules
#stepper modules - cycle control
def StepperCycleUp(stepper_1,stepper_2,sleeptime,cycles):
	for i in range(0,cycles):
		StepperStepUp(stepper_1,stepper_2,sleeptime)
	
def StepperCycleDown(stepper_1,stepper_2,sleeptime,cycles):
	for i in range(0,cycles):
		SteppersTickDown(stepper_1,stepper_2,sleeptime)

#stepper modules - step control
def StepperStepUp(stepper_1,stepper_2,sleeptime):
	stepperRoll_A(stepper_1,sleeptime)
	stepperRoll_B(stepper_2,sleeptime)

def SteppersTickDown(stepper_1,stepper_2,sleeptime):
	stepperRoll_A(stepper_2,sleeptime)
	stepperRoll_B(stepper_1,sleeptime)

#stepper modules - stepper electrical input for roll
def stepperRoll_A(stepper,sleeptime):
	#tick 1
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
	#tick 1
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



#ledfade modules
def ledfade_startup():
	orange.start(100)
	brown.start(100)
	green.start(100)
	yellow.start(100)
	hasLightStarted = True

#def ledfade_execute():

def ledfade_on():
	for i in range(0,101):
		orange.ChangeDutyCycle(i)
		brown.ChangeDutyCycle(i)
		green.ChangeDutyCycle(i)
		yellow.ChangeDutyCycle(i)
		time.sleep(0.02)	


def ledfade_out():
	for i in range(101, -1, -1):
		orange.ChangeDutyCycle(i)
		brown.ChangeDutyCycle(i)
		green.ChangeDutyCycle(i)
		yellow.ChangeDutyCycle(i)
		time.sleep(0.02)


def ledfade_stop():
	orange.stop()
	brown.stop()
	green.stop()
	yellow.stop()
	hasLightStarted = False

#Main program
# print "Starting main program"


#if klep omhoog en licht veranderd dan kelp naar beneden
#loop forever or ctrl^C

#activating the leds
ledfade_startup()
try:
	
	
	while 1==1:
		logwrite("looptick")
		#ldr check check
		if (GPIO.input(17)==1) or GPIO.input(27): #input low active
			#zonlicht aan
		
			sunshine = True
			
			sunshineSTR = str(sunshine)
			hatchStatusSTR = str(hatchStatus)
			hatchMoveSTR = str(hatchMove)
			
			line = "sunlight detected " + sunshineSTR
			logwrite(line)
			
			line = "hatchStatus " + hatchStatusSTR
			logwrite(line)
			
			line = "hatchMove" + hatchMoveSTR
			logwrite(line)
			
			checklightChange()
			
			logwrite("checklight executed")
			line = "sunlight detected " + sunshineSTR
			logwrite(line)
			
			line = "hatchStatus " + hatchStatusSTR
			logwrite(line)
			
			line = "hatchMove " + hatchMoveSTR
			logwrite(line)
			
			time.sleep(1)
			sunRise()
			time.sleep(1) #anti-bouncing
		else:
			#zonlicht uit
			sunshine = False
			
			sunshineSTR = str(sunshine)
			hatchStatusSTR = str(hatchStatus)
			hatchMoveSTR = str(hatchMove)
			
			line = "sunlight detected " + sunshineSTR
			logwrite(line)
			
			line = "hatchStatus " + hatchStatusSTR
			logwrite(line)
			
			line = "hatchMove " + hatchMoveSTR
			logwrite(line)
			
			checklightChange()
			
			logwrite("checklight executed")
			
			sunshineSTR = str(sunshine)
			hatchStatusSTR = str(hatchStatus)
			hatchMoveSTR = str(hatchMove)
			
			line = "sunlight detected " + sunshineSTR
			logwrite(line)
			
			line = "hatchStatus " + hatchStatusSTR
			logwrite(line)
			
			line = "hatchMove " + hatchMoveSTR
			logwrite(line)
			
			time.sleep(1)
			sunSet()
			time.sleep(1) #anti-bouncing

except KeyboardInterrupt:
	#close program
	ledfade_stop()
	GPIO.cleanup()
	logwrite("GPIO cleanup executed")
	file_object.close()
	print("file object closed")




