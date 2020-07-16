#! /usr/bin/env python

import roslib
import rospy
import actionlib

from time import sleep

from dishes_actionlib_example.msg  import DoDishesAction, DoDishesFeedback, DoDishesResult

class DoDishesServer:
	def __init__(self):
		self.server = actionlib.SimpleActionServer('do_dishes', DoDishesAction, self.execute_callback, False)
		self.server.start()

	#def execute(self, goal):
	#	# Do lots of awesome groundbreaking robot stuff here
	#	print(goal)
	#	goal.succeed()
#		self.server.set_succeeded()
	def execute_callback(self, goal_handle):
		#self.get_logger().info('Executing goal...')
		
		dishwasher_id = goal_handle.dishwasher_id
		dishes_to_clean = goal_handle.dishes_to_clean
		print(dishwasher_id, dishes_to_clean)
		feedback_msg = DoDishesFeedback()
		feedback_msg.percent_complete = 0.0

		result_msg = DoDishesResult()
		if dishes_to_clean<=0:
			result_msg.total_dishes_cleaned = 0
		else:
			result_msg.total_dishes_cleaned = 0
			for i in range(0, dishes_to_clean+1): 
				feedback_msg.percent_complete = 100.0 * float(i) /float(dishes_to_clean)
				#self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
				self.server.publish_feedback(feedback_msg)
				print(feedback_msg)
				sleep(.1) # THE operation
				result_msg.total_dishes_cleaned += 1

		self.server.set_succeeded(result_msg)


if __name__ == '__main__':
	rospy.init_node('do_dishes_server')
	server = DoDishesServer()
	rospy.spin()

