import os,sys
from os import curdir,sep,listdir
import re


#LED path
ledpath = '/sys/class/leds/ev3-{}:{}:ev3dev/'
ledbright = ledpath + 'brightness'

#motor definitions
motorAttached = '/sys/class/tacho-motor/'
motorpath = '/sys/class/tacho-motor/{}/'
setMotorSpeed = motorpath + 'duty_cycle_sp'
runMotorPath = motorpath + 'command'
checkMotorPort = motorpath + 'port_name' 

#sensor definitions
sensorpath = '/sys/class/lego-sensor/{}/'
sensorValue = sensorpath + 'value0'
sensorAttached = '/sys/class/lego-sensor/'
checkSensorPort = sensorpath + 'port_name'
sensorModesPath = sensorpath + 'modes'
sensorModePath = sensorpath + 'mode'
drivername = sensorpath + 'driver_name'

soundpath = '/sys/devices/platform/snd-legoev3/{}'

SENSORS = getAllSensors()
print SENSORS

def getAllSensors():
    SENSORS = {}
    try:
        existingSensors = os.listdir(sensorAttached)
        for i in range(0,len(existingSensors)):
            try:
                senRead = open(checkSensorPort.format(existingSensors[i]))
                mo = senRead.read()
                senRead.close
                SENSORS[mo[2]] = existingSensors[i]
            except IOError:
                print "no sensors"
    except IOError: 
        print "no sensors"
    return SENSORS

def getSensor(port):
    port = str(port)
    if port in SENSORS:
        s = open(sensorValue.format(SENSORS[port]))
        value = s.read()
        s.close
        s = open(drivername.format(SENSORS[port]))
        sensor = s.read();
        s.close
        name, units = sensorInfo(sensor)
        return int(value.strip()),name,units
    
def getSensorModes(port):
    port = str(port)
    if port in SENSORS:
        s = open(sensorModesPath.format(SENSORS[port]))
        value = s.read()
        s.close
        return value
    
def changeSensorMode(port,mode):
    port = str(port)
    if port in SENSORS:
        s = open(sensorModePath.format(SENSORS[port]))
        s.write(mode + '\n');
        s.close
    else:
        print "no sensor attached to port {}".format(port)

