from backWheels import BackWheels
import time

myBackWheels = BackWheels()

while True:
  myBackWheels.speed = 30
  myBackWheels.forward()
  time.sleep(1)
  myBackWheels.backward()
  time.sleep(1)
  myBackWheels.speed = 0
  time.sleep(3)
