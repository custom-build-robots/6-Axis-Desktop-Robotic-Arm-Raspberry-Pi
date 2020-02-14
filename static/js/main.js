const url = window.location.protocol + '//' + window.location.hostname + ':' + location.port;
const route_servo = "/set_servo";
const speed_param = "?speed=";
const servo_param = "&servo=";

function get_default() {
    let req = new XMLHttpRequest();
    req.overrideMimeType("application/json");
    req.open('GET', url + '/get-default', true);
    req.onload = function () {
        let jsonResponse = JSON.parse(req.responseText);
        $.each(jsonResponse['servos'], function (index, value) {
            let slider = document.getElementById(value.name);
            let output = document.getElementById(value.name + "_value");
            slider.value = value['values'].default_value;
            slider.min = value['values'].low_value;
            slider.max = value['values'].high_value;
            output.innerHTML = slider.value;
        });
    };
    req.send(null);
}

function servo(slider_id, speed) {
    let output = document.getElementById(slider_id + "_value");
    output.innerHTML = speed;

    let req = new XMLHttpRequest();
    req.overrideMimeType("application/json");
    req.open('GET', url + route_servo + speed_param + speed + servo_param + slider_id, true);
    req.onload = function () {
        console.log(url + route_servo + speed_param + speed + servo_param + slider_id);
    };
    req.send(null);
}

$(document).ready(function(){
    get_default();
});
