import os
import time
print("Waiting for 5 seconds.")
temp = os.popen('sudo python ./arduino.py').read()
print "temp raw: ",temp
time.sleep(7)
temp1 = os.popen('sudo python ./arduino.py').read()
temp = float(temp.strip())
temp1 = float(temp1.strip())
temp2 = os.popen('sudo python ./arduino.py').read()
temp2 = float(temp2.strip())

print "temp: ",temp
print "temp1: ",temp1
print "temp2: ",temp2
print "diff: ", temp-temp2
