from backWheels import BackWheels
import time

myBackWheels = BackWheels()


myBackWheels.speed = 20
myBackWheels.forward()
time.sleep(1)
myBackWheels.backward()
time.sleep(1)
myBackWheels.speed = 0
