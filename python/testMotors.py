# test motors
import ev3
import time

ev3.runMotor('A',100)
time.sleep(3)
ev3.stopMotor('A')
