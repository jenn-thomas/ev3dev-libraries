import ev3
import time

ev3.writeLED('right1','green',0)
ev3.writeLED('left1','green',0)

for i in range(0,256):
    ev3.writeLED('right0','red',str(i))
    ev3.writeLED('left0','red',str(i))
    time.sleep(0.05) 

ev3.writeLED('right0','red',0)
ev3.writeLED('left0','red',0)

for i in range(0,256):
    ev3.writeLED('right1','green',i)
    ev3.writeLED('left1','green',i)
    time.sleep(0.05) 
    
