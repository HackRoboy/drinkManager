# purpose of the below code is to give you a rough idea
 
from roboy_communication_cognition.srv import DescribeScene
import rospy
 
rospy.ServiceProxy('/roboy/cognition/vision/DescribeScene', DescribeScene)
 
def stt_client():
    rospy.wait_for_service("/roboy/cognition/vision/DescribeScene")
    try:
        stt1 = rospy.ServiceProxy('/roboy/cognition/vision/DescribeScene', DescribeScene)
        resp = stt1()

        print "Logger.drinker.py: ",resp
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


