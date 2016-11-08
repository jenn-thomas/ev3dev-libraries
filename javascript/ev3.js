var fs = require('fs');

//paths
var ledpath = '/sys/class/leds/ev3-';
var motorPath = '/sys/class/tacho-motor/'; 
var sensorPath = '/sys/class/lego-sensor/';
var soundPath = '/sys/devices/platform/snd-legoev3/';

// changes on board LEDs ex. writeLED('right1','green',20)
function writeLED(location,color,rgb){
    if ((typeof rgb) != 'string') rgb = rgb.toString();
    var path = ledpath + location + ':' + color + ':ev3dev/brightness';
    fs.writeFileSync(path, rgb);
    return;
}

// writes to motor ex. runMotor('A',100)
function runMotor(port,speed){
    port = port.toUpperCase();
    var num = getPortNumber(port);
    if (num === "") return;
    if ((typeof speed) != 'string') speed = speed.toString();
    var MOTORS = getMotors();
    if (port in MOTORS){
        motorSpeedPath = motorPath + MOTORS[port] + '/duty_cycle_sp';
        motorRunPath = motorPath + MOTORS[port] + '/command';
        fs.writeFileSync(motorSpeedPath, speed + '\n');
        fs.writeFileSync(motorRunPath, 'run-forever');
    }
    else{
        console.log("Run Motor -> no motor connected to port " + port)   
    }
    return;
}

// stops motor ex. stopMotor('A')
function stopMotor(port){
    port = port.toUpperCase();
    var num = getPortNumber(port);
        if (num === "") return;
    var MOTORS = getMotors();
    if (port in MOTORS){
        motorRunPath = motorPath + MOTORS[port] + '/command';
        fs.writeFileSync(motorRunPath, 'stop');
    }
    else {
        console.log("Stop Motor -> No motor connected to port " + port);   
    }
    return;
}

// get sensor values ex. getSensor(1)
// returns array of [value, sensor type, units]
function getSensor(port){
    SENSORS = getAllSensors();
    if ((typeof port) != 'string') port = port.toString();
    if (port in SENSORS){
        var sensorValuePath = sensorPath + SENSORS[port] + '/value0';
        var sensorNamePath = sensorPath + SENSORS[port] + '/driver_name';
        try{
            name = fs.readFileSync(sensorNamePath, 'utf8').trim();
            data = sensorInfo(name);
            value = Number(fs.readFileSync(sensorValuePath,'utf8').trim());
            return [value, data[0], data[1]];
           }
        catch(e){console.log('failed to read sensor');}
    }
    return;
}

function playSound(freq,volume){
    var vPath = soundPath + 'volume';
    var freqPath = soundPath + 'tone';
    fs.writeFileSync(vPath, volume.toString() + '\n');
    fs.writeFileSync(freqPath, freq.toString() +'\n');
}

function stopSound(){
    var freqPath = soundPath + 'tone';
    fs.writeFileSync(freqPath, (0).toString() +'\n');
}

// creates motor object
function getMotors(){
    var existingMotors = fs.readdirSync(motorPath);
    var MOTORS = new Object();
    for (var i = 0; i < existingMotors.length; i++){
        var motorPort = motorPath + existingMotors[i] + "/address";
        try{
            var motorRead = fs.readFileSync(motorPort, "utf8");
            MOTORS[motorRead[3]] = existingMotors[i];
        }
        catch(e){}
    }
    return MOTORS;
}

// creates sensor object
function getAllSensors(){
    var SENSORS = new Object();
    // need an error check here if dir doesnt exist! ***********************************
    try {
        var existingSensors = fs.readdirSync(sensorPath);
        for (var i = 0; i < existingSensors.length; i++){
            var sensorPort = sensorPath + existingSensors[i] + '/port_name';
            try{
                var sensorRead = fs.readFileSync(sensorPort,'utf8')
                SENSORS[sensorRead[2]] = existingSensors[i];
            }
            catch(e){console.log("found no sensors")}
        }
    }
    catch(e){
    }
    return SENSORS;
}

function getPortNumber(port){
    var num;
    switch(port){
        case "A": num = 0; break;
        case "B": num = 1; break;
        case "C": num = 2; break;
        case "D": num = 3; break;
        default: num = ""; break;
    }
    return num;
}

// based on returned sensor name, translate name and get units
function sensorInfo(name){
    if ((name).match('lego-ev3-us') || (name).match('lego-nxt-us')) return ['ultrasonic sensor','cm'];            
    // gyro sensor   
    else if ((name).match('lego-ev3-gyro')) return ['gyro sensor','degrees'];                            
    // touch sensor 
    else if ((name).match('lego-ev3-touch') || (name).match('lego-nxt-touch')) return ['touch sensor','boolean'];                           
    // ir sensor 
    else if ((name).match('lego-ev3-ir')) return ['IR sensor','percent'];                                          
    // color sensor
    else if ((name).match('lego-ev3-color')) return ['color sensor','percent'];
    // unknown sensor
    else return ['unknown sensor',''];
}


