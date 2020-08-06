#! /usr/bin/env python

import roslib
import rospy
import actionlib

from time import sleep

from lisa_interaction_msgs.msg  import LisaUtterAction, LisaUtterFeedback, LisaUtterResult

class LisaUtteranceTestServer:
	"""
	A test class to simulate the behavior of lisa
	"""
	def __init__(self):
		self.server = actionlib.SimpleActionServer('/lisa/say', LisaUtterAction, self.execute_callback, False)
		self.server.start()

	def execute_callback(self, goal_handle):

		sentence = goal_handle.sentence
		print("Uttering: ",sentence)
		feedback_msg = LisaUtterFeedback()
		feedback_msg.percent_complete = 0.0

		for i in range(0, len(sentence)):
			feedback_msg.percent_complete = float(i) /float(len(sentence))
			#self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
			self.server.publish_feedback(feedback_msg)
			print(feedback_msg)
			sleep(.1) # THE operation

		result_msg = LisaUtterResult()
		result_msg.result_message = "Sentence ->{}<- Uttered!".format(sentence)

		self.server.set_succeeded(result_msg)


if __name__ == '__main__':
	rospy.init_node('lisa_utterance_test_server')
	server = LisaUtteranceTestServer()
	rospy.spin()
