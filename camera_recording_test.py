import time
from grovepi import *
from picamera import PiCamera

led = 6
sensor = 5
camera = PiCamera()

def record():
    while digitalRead(sensor) > 1:
        camera.start_recording("footage/myvideo.mp4")
        time.sleep(5)
    camera.stop_recording()






pinMode(led,"OUTPUT")
pinMode(sensor, "INPUT")

while True:
  try:
    movement = digitalRead(sensor)
    if movement > 0:
      print("movement detected")
      record()
    time.sleep(1)

  except IOError:
    print("error")
