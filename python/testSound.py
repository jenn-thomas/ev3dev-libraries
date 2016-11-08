# test sound
import ev3
import time

ev3.playSound(440,1)
time.sleep(0.5)
ev3.stopSound()