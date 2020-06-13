#full code As written by Ben Chermenschi 2020 - ****

#imports
import RPi.GPIO as GPIO
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%d-%m-%Y_%H:%M:%S")
filename = "log-ultrasonic-" + current_time + ".txt"
file_object = open(filename,"w+")


def logwrite(text):
	now = datetime.now()
	current_time = now.strftime("%d-%m-%Y_%H:%M:%S")
	
	output = output = current_time+ " " + text + " \r\n"
	file_object.write(output)
	print(output)
	
logwrite("done")
logwrite("import - complete")

logwrite("preparing for logging")

o= "Current time is "+ current_time
logwrite(o)



#set pins 18 and 

#to use raspberry pi gpio number
GPIO.setmode(GPIO.BCM) #GPIO18

#setting up pins
GPIO.setup(18, GPIO.OUT) #trigger
GPIO.setup(22,GPIO.IN) #echo
GPIO.output(18,0)
logwrite("pin setup complete")
time.sleep(2)



try:
	StartTime = time.time()
	StopTime = time.time()
	while 1==1:
		#set output port 18 high
		GPIO.output(18,1)
		time.sleep(0.00001)
		GPIO.output(18,0)
		
		
	
		#as long as input 22 == low
		while GPIO.input(22) ==0:
			StartTime = time.time()
		while GPIO.input(22) ==1:
			StopTime = time.time()
	
		TimeElapsed = StopTime - StartTime
	
		distance = TimeElapsed * 17150
		distance = round(distance,2)
		strdistance = str(distance)
		now = datetime.now()
		current_time = now.strftime("%d-%m-%Y_%H:%M:%S")
		
		output = current_time+ " Measured distance is "+ strdistance + "\r\n"

		logwrite(output)
		
		time.sleep(2)
		
except KeyboardInterrupt:
	GPIO.cleanup()
	file_object.close()
	print("keyboard interrupt successful")
	
	


	
 
