import RPi.GPIO as GPIO
import time

BtnPin = 12
Led_status = 1

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
def swLed(ev=None):
	global Led_status
	Led_status = not Led_status
	if (Led_status == 1):
		print("led off...")
	else:
		print("...led on")

def loop():
	GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed, bouncetime=200)
	while True:
		time.sleep(1)

def destroy():
		GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()

