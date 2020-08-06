#! /usr/bin/env python

import roslib
# roslib.load_manifest('my_pkg_name')
import rospy
import actionlib
from lisa_interaction_msgs.msg  import LisaUtterAction, LisaUtterGoal


if __name__ == '__main__':
    rospy.init_node('lisa_utter_client')
    client = actionlib.SimpleActionClient('/lisa/say', LisaUtterAction)
    client.wait_for_server()

    goal = LisaUtterGoal(sentence="something to say")
    # Fill in the goal here
    client.send_goal(goal)
    client.wait_for_result(rospy.Duration.from_sec(5.0))

