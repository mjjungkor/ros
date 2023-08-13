import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
from turtlesim.action import RotateAbsolute
from rclpy.action import ActionClient
import sys

MAX_LIN_VEL=0.22
MAX_ANG=2.84

class move_turtle(Node):
    def __init__(self, degree):
        # super().__init__('simple_pub')
        super().__init__('mturtle')
        self.pub=self.create_publisher(Twist, 'turtle1/cmd_vel',10)  
        self.client=ActionClient(self,RotateAbsolute,'turtle1/rotate_absolute') 
        self.create_timer(0.1,self.publisher)
        self.create_timer(0.1,self.update)
        self.dir=-180
        self.speed=1.0
        self.dis=0
        self.num=0

    def call_action(self,degree):
        self.get_logger().info('call action')
        goal_msg=RotateAbsolute.Goal()
        goal_msg.theta=float(degree)*math.pi/180
        self.client.wait_for_server()
        self.send_goal_future=self.client.send_goal_async(goal_msg,feedback_callback=self.feedback_callback)
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
        self.get_logger().info(f'feedback={feedback.remaining}')

    def goal_result_callback(self, future):
        result=future.result().result
        self.get_logger().info(f'result={result.delta}')
        
        
        if result.delta == 0.0:
            self.speed=1.0
            if self.num % 2 == 0:
                self.dir = 0
            else :
                self.dir = -180
            self.num+=1
            self.dis = 0
        #rclpy.shutdown()


    def publisher(self):
        msg=Twist()

        msg.linear.x=self.speed
        #msg.angular.z=self.dir  
        msg = self.restrain(msg)  
        self.pub.publish(msg)
        


    def update(self):
        #터틀을 회전시킬수는 있지만 토픽만으로는 언제 회전을 멈추(회전값 'self.dir=0.0')어야 할지 알수 없음 
        # if self.dis == 50:
        #     self.speed=0.0
        #     self.dir=float(180)*math.pi/180
        # self.dis+=1

        #main안에서 node.call_action(sys.argv[1])을 한번만 호출하면 원하는 각도까지 회전 후 멈추는데
        #spin안에서 call_action을 호출하면 왜 계속 호출해줘야지?
        # (터틀이 회전을 마치지지도 않았는데 result 값이 0.0이 나옴.왜?)

        if self.dis > 50:
            self.speed=0.0
            self.get_logger().info(F'trun {self.dir} degree')
            
            self.call_action(self.dir)
        self.dis += 1

        # self.speed+=0.001*self.dir
        # if self.speed>2:
        #     self.dir=-1.0
        # elif self.speed<0:
        #     self.dir=1.0

    def restrain(self,msg):        
        if msg.linear.x<-MAX_LIN_VEL:
            msg.linear.x=-MAX_LIN_VEL
        elif msg.linear.x>MAX_LIN_VEL:
            msg.linear.x=MAX_LIN_VEL

        if msg.angular.z<-MAX_ANG:
            msg.angular.z=-MAX_ANG
        elif msg.angular.z>MAX_ANG:
            msg.angular.z=MAX_ANG

        return msg


def main():
    rclpy.init()
    node=move_turtle(sys.argv[1])
        
    try:
        #node.call_action(sys.argv[1])
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('KeyboardInterrupt Error')
    finally:
        node.destroy_node
        rclpy.shutdown()
    print('This is test')

if __name__=='__main__':
    main()