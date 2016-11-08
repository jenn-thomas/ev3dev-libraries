var keycodes = {37: "left arrow", 38: "up arrow", 39: "right arrow", 40: "down arrow",
                65: "a", 66: "b", 67: "c", 68: "d", 69: "e", 70: "f", 71: "g", 72: "h", 73: "i", 74: "j", 
                75: "k", 76: "l", 77: "m", 78: "n", 79: "o", 80: "p", 81: "q", 82: "r", 83: "s", 84: "t",
               85: "u", 86: "v", 87: "w", 88: "x", 89: "y", 90: "z"}

//deal with communication with the server
function xml_http_post(url, data, callback) {
    var req = false;
    try {
        // Firefox, Opera 8.0+, Safari
        req = new XMLHttpRequest();
    }
    catch (e) {
        // Internet Explorer
        try {
            req = new ActiveXObject("Msxml2.XMLHTTP");
        }
        catch (e) {
            try {
                req = new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch (e) {
                alert("Your browser does not support AJAX!");
                return false;
            }
        }
    }
    req.open("POST", url, true);
    req.onreadystatechange = function() {
        if (req.readyState == 4 && req.status==200) {
            callback(req);
        }
    }
    req.send(data);
}

//get response from server (callback)
function test_handle(req) {
    console.log(req)
}

function controlMotors(){
    var rMotor = document.getElementById('rightMotor').value;
    var lMotor = document.getElementById('leftMotor').value;
}