var ev3 = require('ev3');

ev3.writeLED('right1','green',0);
ev3.writeLED('left1','green',0);

for (var i;i<256;i++){
    ev3.writeLED('right0','red',i.toString());
    ev3.writeLED('left0','red',i.toString());
}

ev3.writeLED('right0','red',0);
ev3.writeLED('left0','red',0);

for (var i;i<256;i++){
    ev3.writeLED('right1','green',i);
    ev3.writeLED('left1','green',i);
}