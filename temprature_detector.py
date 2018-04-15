from roboy_communication_cognition.srv import Talk
import rospy
import os
import bottle_detector
import time
rospy.ServiceProxy('/roboy/cognition/speech/synthesis/talk', Talk)
 
good_coffee_temprature_diff = 1.5
good_beer_temprature_diff = 2
def stt_client(var):
	rospy.wait_for_service("/roboy/cognition/speech/synthesis/talk")
	try:
        	stt = rospy.ServiceProxy('/roboy/cognition/speech/synthesis/talk',Talk)
		#detected_os = objects.popen('python ./drinker.py').read()
		#print "Logger.info.temperature: ", temp	
		#print "Logger.info.detected_objects: ",detected_objects
		#while True:
		if var == "both":
			stt("OH! I see some of you drinking beer and others coffee.")
			stt("Let me check if it is enough cold for drinking beer. Please put it on detector and wait 5 second.")
			temp = os.popen('sudo python ./arduino.py').read()
			time.sleep(5)
			temp1 = os.popen('sudo python ./arduino.py').read()
			temp2 = os.popen('sudo python ./arduino.py').read()
			temp2 = float(temp2.strip())
			temp = float(temp.strip())
			temp1 = float(temp1.strip())
			if temp-temp2 < float(good_beer_temprature_diff):
				print "dif: ",temp-temp1
				if temp-temp2 > float(1.5):
					resp = stt("You have to keep it 10 minutes in the fridge")
				elif temp-temp2 > float(1.0):
					resp = stt("You have to keep it 20 minutes in the fridge")
				elif temp-temp2 > float(0.5):
					resp = stt("You have to keep it 30 minutes in the fridge")
				else:
					resp = stt("You have to keep it 1 hour in the fridge")
				resp = stt("This beer is not cold enough")
			else:
				print "dif: ",temp1-temp
				resp = stt("This beer is cold enough, cheers")
				
			stt("It is time to check Coffee. Please put it on detector and wait 5 second.")
			temp = os.popen('sudo python ./arduino.py').read()
			time.sleep(5)
			temp1 = os.popen('sudo python ./arduino.py').read()
			temp2 = os.popen('sudo python ./arduino.py').read()
			temp2 = float(temp2.strip())
			temp = float(temp.strip())
			temp1 = float(temp1.strip())
			print "temp: ",temp
			print "temp2: ",temp2
			if temp2-temp < float(good_coffee_temprature_diff) :
				print "dif: ",temp1-temp
				resp = stt("This coffee is too cold.")
			else:
				print "dif: ",temp-temp1
				resp = stt("This is really hot. Now you can start coding. Have fun! ")
			
       			print "logger.talk.response: ",resp
       			return resp
		elif var == "beer":
			stt("OH! I see you are drinking beer.")
			stt("Let me check if it is enough cold for drinking. Please put it on detector and wait 5 second.")
			temp = os.popen('sudo python ./arduino.py').read()			
			time.sleep(5)
			temp1 = os.popen('sudo python ./arduino.py').read()
			temp2 = os.popen('sudo python ./arduino.py').read()
			temp2 = float(temp2.strip())
			temp = float(temp.strip())
			temp1 = float(temp1.strip())
			print("temp: ",temp)
			if temp-temp2 < float(good_beer_temprature_diff):
				print "dif: ",temp-temp2
				if temp-temp2 > float(1.5):
					resp = stt("You have to keep it 10 min in the fridge")
				elif temp-temp2 > float(1.0):
					resp = stt("You have to keep it 20 min in the fridge")
				elif temp-temp2 > float(0.5):
					resp = stt("You have to keep it 30 min in the fridge")
				else:
					resp = stt("You have to keep it 1 hour in the fridge")
				resp = stt("This beer is not cold enough")
			else:
				print "dif: ",temp-temp2
				resp = stt("This beer is cold enough, cheers")
			print "logger.talk.response: ",resp
       			return resp

		elif var == "cup":
			stt("OH! I see you are drinking coffee.")
			stt("Let me check if it is nice to drink.Please put it on detector and wait 5 second.")
			print("Let me check if it is nice to drink.")
			temp = os.popen('sudo python ./arduino.py').read()			
			time.sleep(5)
			temp1 = os.popen('sudo python ./arduino.py').read()
			temp2 = os.popen('sudo python ./arduino.py').read()
			temp2 = float(temp2.strip())
			temp = float(temp.strip())
			temp1 = float(temp1.strip())
			print("temp: ",temp)
			print "temp2: ",temp2
			if temp2-temp < float(good_coffee_temprature_diff):
				print "dif: ",temp2-temp 
				resp = stt("This coffee is too cold.")
			else:
				print "dif: ",temp2-temp
				resp = stt("This is really hot. Now you can start coding. Have fun! ")
				
			#print "logger.talk.response: ",resp
			return ""
		
		else:
			resp = stt("I can't detect anything. Could you please be closer?")
		#print "logger.error.detected_objects: bottle_detector doesn't work! "
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def vision_client():
	os.system('export ROS_MASTER_URI=http://129.187.142.46:11311')
	detected_objects = bottle_detector.stt_client().objects_detected
	print "assadasdas",detected_objects 
	if detected_objects:
		if "bottle" in detected_objects and "cup" in detected_objects:
        		return "both"
		elif "bottle" in detected_objects:
			return "beer"

		elif "cup" in detected_objects:
			return "cup"
		
		else:
			return "none"
	else:
		return "empty"
		#print "logger.error.detected_objects: bottle_detector doesn't work! "
if __name__ == "__main__":
	while True:
		var = vision_client()
		#print "var::::  ",var
		#print "type var::::  ",type(var.text)
		#var="beer"
		stt_client(var)
		raw_input('Press enter to continue: ')	
