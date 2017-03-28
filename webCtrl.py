

import urllib2
import serial
from time import sleep
import math
from flask import Flask, render_template, request
app = Flask(__name__)

ser = serial.Serial('/dev/ttyS0',9600, timeout=1) #establish serial connection

directions = [
   'forward',
   'left',
   'right',
   'reverse',
   'stop'
   ]

@app.route("/")
def main():
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'directions' : directions
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

@app.route("/direction/<direction>")
def move(direction):
   if direction == "forward":
      ser.write(chr(235))
      ser.write(chr(107))
      #do something
   if direction == "right":
      ser.write(chr(int('100'))) #motor1 1/2 speed forward (91)
      ser.write(chr(int('155'))) #motor2 1/2 speed reverse  (160)
      #do something
   if direction == "left":
      ser.write(chr(int('224' ))) #motor2 1/2 speed forward
      ser.write(chr(int('32'))) #motor2 1/2 speed reverse
      
      #do something
   if direction == "stop":
      ser.write(chr(0))
      #stop doing something
   if direction == "reverse":
      ser.write(chr(int('32')))
      ser.write(chr(int('155')))
      #stop doing something   

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'directions' : directions
   }

   return render_template('main.html', **templateData)
   

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
