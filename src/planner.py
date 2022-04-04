import rospy
import cv2
import time

from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
command_pub = rospy.Publisher("motor_commands",String)
h = 600
l = 375
r = 425
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
  global r, l
  try:
    cv_image = bridge.imgmsg_to_cv2(data,"bgr8")
    print(cv_image.shape)

    gray_image = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
    command = plan(gray_image[h][l], gray_image[h][r])
    if command == "STOP":
      print ("SSSS")
      for l in range (0,800):
        r = r+25
        l = l-25
        command = plan(gray_image[h][r], gray_image[h][l])
        if command == "STOP":
          command_pub.publish("BACK")
          time.sleep(0.5)

        
    
    gray_image = cv2.line(gray_image, (300,h), (500,h), 0 , 5)
    if command == "RIGHT":
      gray_image = cv2.circle(gray_image, (500, h), 5, 255 ,2)    
    if command == "LEFT":
      gray_image = cv2.circle(gray_image, (300, h), 5, 255 ,2)    
    if command == "GO":
      gray_image = cv2.circle(gray_image, (400, h), 5, 255 ,2)
    if command == "BACK":
      gray_image = cv2.circle(gray_image, (400, h), 5, 255 ,5)
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

