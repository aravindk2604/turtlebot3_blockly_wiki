import rospy, sys
import time
from geometry_msgs.msg import Twist

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
#rospy.init_node('circle_mode', anonymous=True)
rate = rospy.Rate(10) # 10Hz
twist = Twist()
start = time.time()
flag=True #time flag
# Angular velocity = linear velocity / radius
speed=dropdown_speed # SLOW, NORMAL, FAST
twist.linear.z = 0.00

# CLOCKWISE rotation
if speed =='SLOW':
    twist.linear.y = 0.05
    twist.linear.x = 0.05
elif speed =='NORMAL':
    twist.linear.y = 0.25
    twist.linear.x = 0.25
elif speed == 'FAST':
    twist.linear.y = 0.75
    twist.linear.x = 0.75
while not rospy.is_shutdown() and flag:
    sample_time=time.time()
    if ((sample_time - start) > 3):
      flag=False
    pub.publish(twist)
twist = Twist()
pub.publish(twist)
rate.sleep()
