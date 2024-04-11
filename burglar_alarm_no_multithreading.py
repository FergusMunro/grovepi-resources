import time
from grovepi import *
import threading

def flash_light(led, flashes, period):
    for i in range(flashes):
        digitalWrite(led, 1)
        time.sleep(period)
        digitalWrite(led, 0)
        time.sleep(period)

led = 6
sensor = 5

pinMode(led,"OUTPUT")
pinMode(sensor, "INPUT")

while True:
  try:
    movement = digitalRead(sensor)
    if movement > 0:
      print("movement detected")
      flash_light(led, 3, 0.4)

  except IOError:
    print("error")
