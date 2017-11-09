from flask import Flask
from flask import request

import time
#import atexit

# Importiere die Adafruit PCA9685 Bibliothek
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
PCA9685_pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Set frequency to 100hz, good for l298n h-bridge.
PCA9685_pwm.set_pwm_freq(60)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

app = Flask(__name__)

@app.route("/")
def web_interface():
  html = open("index.html")
  response = html.read().replace('\n', '')
  html.close()
  return response

@app.route("/set_servo1")  
def set_servo1():  
  speed = request.args.get("speed")
  print "Received " + str(speed)
  PCA9685_pwm.set_pwm(0, 0, int(speed))
  return "Received " + str(speed)   
  
@app.route("/set_servo2")  
def set_servo2():  
  speed = request.args.get("speed")
  print "Received " + str(speed)
  PCA9685_pwm.set_pwm(1, 0, int(speed))  
  return "Received " + str(speed)  

@app.route("/set_servo3")  
def set_servo3():  
  speed = request.args.get("speed")
  print "Received " + str(speed)
  PCA9685_pwm.set_pwm(2, 0, int(speed))  
  return "Received " + str(speed) 

@app.route("/set_servo4")  
def set_servo4():  
  speed = request.args.get("speed")
  print "Received " + str(speed)
  PCA9685_pwm.set_pwm(3, 0, int(speed))  
  return "Received " + str(speed) 
 
@app.route("/set_servo5")  
def set_servo5():  
  speed = request.args.get("speed")
  print "Received " + str(speed)
  PCA9685_pwm.set_pwm(4, 0, int(speed))  
  return "Received " + str(speed) 

@app.route("/set_servo6")  
def set_servo6():  
  speed = request.args.get("speed")
  print "Received " + str(speed)
  PCA9685_pwm.set_pwm(5, 0, int(speed))  
  return "Received " + str(speed)   
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181, debug=True)
