import os,sys
from os import curdir,sep,listdir
import re
import json

#motor definitions
motorAttached = '/sys/class/tacho-motor/'
motorpath = '/sys/class/tacho-motor/{}/'
setMotorSpeed = motorpath + 'duty_cycle_sp'
runMotorPath = motorpath + 'command'
checkMotorPort = motorpath + 'port_name' 