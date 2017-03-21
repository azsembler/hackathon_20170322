#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def move_callback(message):
    command = message.data.lower()
    twist = Twist()

    if  command == "forward":
        rospy.loginfo("Moving forward ...")
        twist.linear.x = 0.1

    elif command == "backward":
        rospy.loginfo("Moving backward ...")
        twist.linear.x = -0.1

    elif command == "left":
        rospy.loginfo("Moving left ...")
        twist.linear.x = 0.1
        twist.angular.z = 0.2

    elif command == "right":
        rospy.loginfo("Moving right ...")
        twist.linear.x = 0.1
        twist.angular.z = -0.2

    elif command == "stop":
        rospy.loginfo("Stoping ...")
        twist.linear.x = 0
        twist.angular.z = 0


    gazebo_publisher.publish(twist)

def main():
    global gazebo_publisher

    rospy.init_node('controller')
    rospy.Subscriber('/input', String, move_callback)

    gazebo_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()
    pass

if __name__ == '__main__':
    main()
