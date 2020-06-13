#imports
import RPi.GPIO as GPIO
import time

#pre-run cleanup


#setup PI GPIO numbers
GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#assigning pins to wire colors for better control
orange = GPIO.PWM(12,100)
brown = GPIO.PWM(16,100)
green = GPIO.PWM(20,100)
yellow = GPIO.PWM(21,100)

#pausetime to speed up or slow down the pulse
pause_time = 0.02

#setting start values
orange.start(0)
brown.start(0)
green.start(0)
yellow.start(0)

try:
	while True:
		for i in range(0,101):
			orange.ChangeDutyCycle(i)
			brown.ChangeDutyCycle(100 - i)
			time.sleep(pause_time)
		for i in range(100, -1, -1):
			orange.ChangeDutyCycle(i)
			brown.ChangeDutyCycle(100 - i)
			time.sleep(pause_time)

except KeyboardInterrupt:
	orange.stop()
	brown.stop()
	green.stop()
	yellow.stop()
	GPIO.cleanup()

