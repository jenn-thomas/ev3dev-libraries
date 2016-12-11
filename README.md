# EV3DEV Libraries

Javascript and python libraries to control the motor and sensor ports on the [ev3dev](http://www.ev3dev.org/)

The main library functions for javascript and python are in their respective folders and are titled ev3. The remaining files are examples showing how these libraries are used.

**Warning**: The ev3dev software is in development and the file paths to the motors and sensors occasionally change. This would cause the libraries to throw an error.

#### Javascript Library Functions

- writeLED(location, color, rgb)
 - changes on board LEDs ex. writeLED('right1','green',20)
- runMotor(port, speed)
 - writes to motor to continuously turn it on ex. runMotor('A',100)
- stopMotor(port)
 - stops a currently running motor ex. stopMotor('A')
- getSensor(port)
 - get sensor values ex. getSensor(1), returns array of [value, sensor type, units]
- playSound(freq, volume)
 - plays a sound
- stopSound()
 - stops a currently playing sound
 
#### Python Library Functions
- writeLED(location, color, rgb)
 - changes on board LEDs ex. writeLED('right1','green',20)
- runMotor(port, speed)
 - writes to motor to continuously turn it on ex. runMotor('A',100)
- stopMotor(port)
 - stops a currently running motor ex. stopMotor('A')
- getSensor(port)
 - get sensor values
 - returns int value, driver name, and mode, examples: ultrasonic, gyro, touch, IR, color
- playSound(freq, volume)
 - plays a sound
- stopSound()
 - stops a currently playing sound
