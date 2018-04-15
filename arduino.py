
"""
Created on Thu Aug 17 13:25:46 2017

@author: glassbox
"""

"""Module importation"""
import serial

"""Opening of the serial port"""
try:
    arduino = serial.Serial("/dev/ttyACM0", 115200)
except:
    print('Please check the port')


"""Initialising variables""" 
rawdata=[]
var = 0
"""Receiving data and storing it in a list"""
def temp():
    rawdata.append(str(arduino.readline()))
    return str(arduino.readline()) 


print temp()

