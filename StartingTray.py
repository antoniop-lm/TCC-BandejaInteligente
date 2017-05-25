import RPi.GPIO as GPIO
import time
import os

FstBtnPin = 12
SndBtnPin = 16
TrdBtnPin = 18

RedLedPin = 11
GreenLedPin = 13
YellowLedPin = 15

RedLed_status = 1
GreenLed_status = 1
YellowLed_status = 1

def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(RedLedPin, GPIO.OUT)
  GPIO.setup(GreenLedPin, GPIO.OUT)
  GPIO.setup(YellowLedPin, GPIO.OUT)
  GPIO.setup(FstBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(SndBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(TrdBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.output(RedLedPin, GPIO.HIGH)
  GPIO.output(GreenLedPin, GPIO.HIGH)
  GPIO.output(YellowLedPin, GPIO.HIGH)	

def scanQRCode(ev=None):
  global RedLed_status
  RedLed_status = not RedLed_status
  GPIO.output(RedLedPin, RedLed_status)
  os.system("/home/pi/Documents/TCC/QRCode.sh")
  RedLed_status = not RedLed_status
  GPIO.output(RedLedPin, RedLed_status)

def findMedicalTray(ev=None):
  global GreenLed_status
  GreenLed_status = not GreenLed_status
  GPIO.output(GreenLedPin, GreenLed_status)
  os.system("/home/pi/Documents/TCC/WiFi.sh")
  GreenLed_status = not GreenLed_status
  GPIO.output(GreenLedPin, GreenLed_status)

def shutdownMedicalTray(ev=None):
  global YellowLed_status
  YellowLed_status = not YellowLed_status
  GPIO.output(YellowLedPin, YellowLed_status)
  print("The system will be shutdown. Thank you for using this aplication.")
  time.sleep(0.5)
  destroy()
  os.system("sudo poweroff")

def loop():
  GPIO.add_event_detect(FstBtnPin, GPIO.FALLING, callback=scanQRCode, bouncetime=200)
  GPIO.add_event_detect(SndBtnPin, GPIO.FALLING, callback=findMedicalTray, bouncetime=200)
  GPIO.add_event_detect(TrdBtnPin, GPIO.FALLING, callback=shutdownMedicalTray, bouncetime=200)
  while True:
    time.sleep(1)

def destroy():
  GPIO.output(RedLedPin, GPIO.HIGH)
  GPIO.output(GreenLedPin, GPIO.HIGH)
  GPIO.output(YellowLedPin, GPIO.HIGH)
  GPIO.cleanup()

def running():
  global RedLed_status
  RedLed_status = not RedLed_status
  GPIO.output(RedLedPin, RedLed_status)
  global GreenLed_status
  GreenLed_status = not GreenLed_status
  GPIO.output(GreenLedPin, GreenLed_status)
  global YellowLed_status
  YellowLed_status = not YellowLed_status
  GPIO.output(YellowLedPin, YellowLed_status)
  time.sleep(3)
  RedLed_status = not RedLed_status
  GPIO.output(RedLedPin, RedLed_status)
  GreenLed_status = not GreenLed_status
  GPIO.output(GreenLedPin, GreenLed_status)
  YellowLed_status = not YellowLed_status
  GPIO.output(YellowLedPin, YellowLed_status)

if __name__ == "__main__":
  setup()
  running()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()
