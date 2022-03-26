import rospy
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
command_pub = rospy.Publisher("motor_commands",String)

def isWhite(val):
 return val > 100
def plan(left, right):

  threshold_val = 120
  command = "STOP"
  if isWhite(left) and not isWhite(right):
    command = "LEFT"
  if isWhite(right) and not isWhite(left):
    command = "RIGHT"
  if isWhite(left) and isWhite(right):
    command = "GO"
  if not isWhite(right) and not isWhite(left):
    command = "BACK"
#  else:
#    while not isWhite(right) and not isWhite(left):
#      command = "STOP"
#      left = left - 10
#      right = right + 10
#      if isWhite(left) and not isWhite(right):
#        command = "LEFT"
#      if isWhite(right) and not isWhite(left):
#        command = "RIGHT"
#      if isWhite(left) and isWhite(right):
#        command = "GO"
#      print(left, right, command)
#      command_pub.publish(command)

  print(left, right, command)
  command_pub.publish(command)
  return command
  
def imgCallback(data):
  try:
    cv_image = bridge.imgmsg_to_cv2(data,"bgr8")
    print(cv_image.shape)
    l = 300
    r = 500
    gray_image = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
    command = plan(gray_image[700][l], gray_image[700][r])
    cv2.line(gray_image, (l,700), (r,700), 0 , 5)
    if command == "STOP":
      if r < 800 and l > 0:
        r = r+50
        l = l-50
        command = plan(gray_image[700][r], gray_image[700][l])
        cv2.line(gray_image, (l,700), (r,700), 0 , 5)
      else:
        command_pub.publish("BACK")
        cv2.line(gray_image, (l,750), (r,750), 0 , 5)

        
    
    
    
    cv2.imshow("Raw Image", gray_image)
    cv2.waitKey(3)
    
    

    
  except CvBridgeError as e:
    print(e)
  
def main():
  print("Hey Universe!")
  rospy.init_node('my_planner_node')
  img_sub = rospy.Subscriber("/camera/image_raw",Image,imgCallback)
  rospy.spin()
 
if __name__ == "__main__":
  main()

