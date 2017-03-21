#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

gazeboOn = False

def move_callback(message):
    command = message.data.lower()
    twist = Twist()

    rospy.loginfo("Swith is %s" %("ON" if gazeboOn else "OFF"))

    if gazeboOn:
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

    else:
        rospy.loginfo("Gazebo is turned off ...")


    gazebo_publisher.publish(twist)

def trigger_callback(message):
    global gazeboOn
    command = message.data.lower()

    if command == "e_start":
        rospy.loginfo("Turning on ...")
        gazeboOn = True
    elif command == "e_stop":
        rospy.loginfo("Turning off ...")
        gazeboOn = False

        twist = Twist()

        twist.linear.x = 0
        twist.angular.z = 0

        gazebo_publisher.publish(twist)


def main():
    global gazebo_publisher

    rospy.init_node('controller')
    rospy.Subscriber('/input', String, move_callback)

    rospy.Subscriber('/event_in', String, trigger_callback)

    gazebo_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()
    pass

if __name__ == '__main__':
    main()
