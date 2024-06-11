import time
from grovepi import *
from picamera import PiCamera
from datetime import datetime

sensor = 5
camera = PiCamera()
pinMode(sensor, "INPUT")

def takePhoto():
    camera.start_preview()
    time.sleep(2)
    camera.capture('photos/%.jpg' % formatFile())
    camera.stop_preview()

def formatFile():
  now = datetime.now()
  fileName = now.strftime("%Y-%M-%D.%H-%M-%S")
  return fileName

while True:
  try:
    movement = digitalRead(sensor)
    if movement > 0:
      print("movement detected")
      takePhoto()
      time.sleep(14)
    time.sleep(1)

  except IOError:
    print("error")
