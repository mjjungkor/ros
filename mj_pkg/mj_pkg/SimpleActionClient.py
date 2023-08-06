import rclpy
import random
from rclpy.node import Node
from mj_interfaces.action import Fibonacci
from rclpy.action import ActionClient
import sys

class Simple_action_client(Node):
    def __init__(self):
        super().__init__('fibonacci_cli')
        self.client=ActionClient(self,Fibonacci,'fibonacci')
        
    def call_action(self,step):        
        goal_message=Fibonacci.Goal()
        goal_message.step=int(step)
        self.client.wait_for_server()
        self.send_goal_future=self.client.send_goal_async(goal_message, feedback_callback=self.feedback_callback)
        self.send_goal_future.add_done_callback(self.goal_resopnse_callback)

    def goal_resopnse_callback(self, future):
        goal_handle=future.result()
        if not goal_handle.accepted:
            self.get_logger().warn('Goal Rejeted!')
            return
        self.get_logger().info('Goal Accepted!')
        self.get_result_future=goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.goal_result_callback)

    
    def feedback_callback(self,feedback_message):
        feedback=feedback_message.feedback
        self.get_logger().info(f'feedback={feedback.temp_seq}')

    def goal_result_callback(self, future):
        result=future.result().result
        self.get_logger().info(f'result={result.seq}')
        rclpy.shutdown()#완료되면 spin에서 벗어나서 강제로 종료


def main():
    rclpy.init()
    node=Simple_action_client()

    try:
        node.call_action(sys.argv[1])
        rclpy.spin(node)
        
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()