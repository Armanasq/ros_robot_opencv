import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

def isWhite(val):
 return val > 120
def plan(left, right):
  print(left, right)
  threshold_val = 120
  if isWhite(left) and not isWhite(right):
    print("LEFT")
  if isWhite(right) and not isWhit(left):
    print("RIGHT")
  if isWhite(left) and isWhite(right):
    print("GO")
    
def imgCallback(data):
  try:
    cv_image = bridge.imgmsg_to_cv2(data,"bgr8")
    print(cv_image.shape)
    gray_image = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
    plan(gray_image[700][300], gray_image[700][500])
    cv2.line(gray_image, (300,700), (500,700), 0 , 5)
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

