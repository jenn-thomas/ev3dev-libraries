import ev3
import time

port = 4
modes = ev3.getSensorModes(port).split()
print modes
for i in range(0,len(modes)):
    ev3.setSensorMode(port,modes[i])
    print modes[i]
    print ev3.getSensor(port)
    time.sleep(0.1)
    
