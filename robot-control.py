import time
import json

from flask import Flask
from flask import request
from flask_cors import CORS

DEBUG = False

if not DEBUG:
    import Adafruit_PCA9685
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(60)

# load servo config
with open('config.json') as f:
    servos_dict = json.load(f)
    f.close()

app = Flask(__name__, static_url_path='/static')
CORS(app)


@app.route("/")
def web_interface():
    html = open("index.html")
    calibrate()
    response = html.read().replace('\n', '')
    html.close()
    return response


@app.route("/get-default")
def get_default():
    return servos_dict


@app.route("/calibrate", methods=['POST'])
def calibrate():
    # calibration
    print('Calibrate robot ....')
    try:
        for servo in servos_dict['servos']:
            print('Calibrate Servo {}: {} with default value: {}'.format(servo['id'], servo['name'],
                                                                         servo['values']['default_value']))
            if not DEBUG:
                pwm.set_pwm(servo['id'], 0, servo['values']['default_value'])
            time.sleep(2)
    except Exception as e:
        print(e)
    html = open("index.html")
    response = html.read().replace('\n', '')
    html.close()
    return response


@app.route("/set_servo")
def set_servo():
    speed = int(request.args.get("speed"))
    servo = request.args.get("servo")
    low_value = 0
    high_value = 0
    servo_id = ''

    for item in servos_dict['servos']:
        if item['name'] == servo:
            servo_id = int(item['id'])
            low_value = int(item['values']['low_value'])
            high_value = int(item['values']['high_value'])

    print('Configure servo: {} ...'.format(servo))
    print('Low: {} | High: {}'.format(low_value, high_value))
    print('Received value: {}'.format(speed))

    if speed > high_value or speed < low_value:
        print('Value: {} too low or too high'.format(speed))
        return "Value too low or too high"
    else:
        print('Set value: {}'.format(speed))
        if not DEBUG:
            pwm.set_pwm(servo_id, 0, speed)
    return "Received " + str(speed)
