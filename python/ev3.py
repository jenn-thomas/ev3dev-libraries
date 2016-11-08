# ev3dev python library for LEDs, sensors, and motors
# current functions:
#   writeLED(location,color,rgb)
#   runMotor(port,speed)
#   stopMotor(port)
#   getSensor(port)
#       returns int value, driver name, and mode
#       examples: ultrasonic, gyro, touch, IR, color
#   playSound(freq,volume)
#   stopSound()

import os,sys
from os import curdir,sep,listdir
import re


#LED path
ledpath = '/sys/class/leds/ev3-{}:{}:ev3dev/'
ledbright = ledpath +'brightness'

#motor definitions
motorAttached = '/sys/class/tacho-motor/'
motorpath = '/sys/class/tacho-motor/{}/'
setMotorSpeed = motorpath + 'duty_cycle_sp'
runMotorPath = motorpath + 'command'
checkMotorPort = motorpath + 'address'

#sensor definitions
sensorpath = '/sys/class/lego-sensor/{}/'
sensorValue = sensorpath + 'value0'
sensorAttached = '/sys/class/lego-sensor/'
checkSensorPort = sensorpath + 'address'
sensorModesPath = sensorpath + 'modes'
sensorModePath = sensorpath + 'mode'
drivername = sensorpath + 'driver_name'

soundpath = '/sys/devices/platform/snd-legoev3/{}'


# turn on/off LED ex. writeLED('left1','green',20)
# *********** maybe just left/right and convert? *******
def writeLED(location,color,rgb):
    if ~(type(rgb) is str):
        rgb = str(rgb)
    LED = open(ledbright.format(location,color),"w",0)
    LED.write(rgb + '\n')
    LED.close

def getMotors():
    existingMotors = os.listdir(motorAttached)
    MOTORS = {}
    for i in range(0,len(existingMotors)):
        try:
            motorRead = open(checkMotorPort.format(existingMotors[i]))
            mo = motorRead.read()
            motorRead.close
            MOTORS[mo[3]] = existingMotors[i]
        except IOError:
            print "no motor"
    return MOTORS

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

def getPortNumber(port):
    if port == "A":
        num = 0
    elif port == "B":
        num = 1
    elif port == "C":
        num = 2
    elif port == "D":
        num = 3
    else:
        num = ''
    return num

def sensorInfo(name):
    if name.find('lego-ev3-us') == 0 or name.find('lego-nxt-us') == 0:
        return 'ultrasonic sensor','cm'
    # gyro sensor
    elif name.find('lego-ev3-gyro') == 0:
        return 'gyro sensor','degrees'
    # touch sensor
    elif name.find('lego-ev3-touch') == 0 or name.find('lego-nxt-touch') == 0:
        return 'touch sensor','boolean'
    # ir sensor
    elif name.find('lego-ev3-ir') == 0:
        return 'IR sensor','percent'
    # color sensor
    elif name.find('lego-ev3-color') == 0:
        return 'color sensor','percent'
    # unknown sensor
    else:
        return 'unknown sensor',''

# turn motor on ex. runMotor('A',100)
def runMotor(port,speed):
    port = port.upper()
    num = getPortNumber(port)
    if num == "":
        print "please enter correct motor port"
        return
    if ~(type(speed) is str):
        speed = str(speed)
    MOTORS = getMotors()
    if port in MOTORS:
        motor = open(setMotorSpeed.format(MOTORS[port]),"w",0)
        motor.write(speed + '\n')
        motor.close
        motor = open(runMotorPath.format(MOTORS[port]),"w",0)
        motor.write('run-forever')
        motor.close
    else:
        print "no motor attached to port {}".format(port)

def stopMotor(port):
    num = getPortNumber(port)
    if num == "":
        print "please enter correct motor port"
        return
    MOTORS = getMotors()
    if port in MOTORS:
        motor = open(runMotorPath.format(MOTORS[port]),"w",0)
        motor.write("stop")
        motor.close
    else:
        print "no motor attached to port {}".format(port)

def getSensor(port):
    SENSORS = getAllSensors()
    if ~(type(port) is str):
        port = str(port)
    if port in SENSORS:
        s = open(sensorValue.format(SENSORS[port]))
        value = s.read()
        s.close
        s = open(drivername.format(SENSORS[port]))
        sensor = s.read();
        s.close
        # name = sensorInfo(sensor)
        units = getSensorMode(port)
        return int(value.strip()),sensor.strip(),units.strip()

def getSensorModes(port):
    SENSORS = getAllSensors()
    if ~(type(port) is str):
        port = str(port)
    if port in SENSORS:
        s = open(sensorModesPath.format(SENSORS[port]))
        value = s.read()
        s.close
        return value

def setSensorMode(port,mode):
    SENSORS = getAllSensors()
    if ~(type(port) is str):
        port = str(port)
    if port in SENSORS:
        s = open(sensorModePath.format(SENSORS[port]),"w",0)
        try:
            s.write(mode + '\n')
        except IOError:
            print IOError
        s.close

def getSensorMode(port):
    SENSORS = getAllSensors()
    if ~(type(port) is str):
        port = str(port)
    if port in SENSORS:
        s = open(sensorModePath.format(SENSORS[port]))
        value = s.read()
        s.close
        return value

def playSound(freq,volume):
    s = open(soundpath.format('volume'),"w",0)
    s.write(str(volume) + '\n')
    s.close()
    s = open(soundpath.format('tone'),"w",0)
    s.write(str(freq) + '\n')

def stopSound():
    s = open(soundpath.format('tone'),"w",0)
    s.write(str(0) + '\n')
