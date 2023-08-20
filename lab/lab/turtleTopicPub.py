import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.callback_groups import ReentrantCallbackGroup
import math

class Message_Publisher(Node):
    def __init__(self):
        super().__init__('move_turtle')
        self.create_subscription(Pose, 'turtle1/pose', self.subcallback, 10,callback_group=ReentrantCallbackGroup())
        self.pub=self.create_publisher(Twist, 'turtle1/cmd_vel',10,callback_group=ReentrantCallbackGroup())
        self.create_timer(0.01,self.publisher)
        self.cur_x=0
        self.target_x=0.0
        self.step=0.5 #step을 param으로 사용하도록 코드 고도화

    #터틀이동Topic발행
    def publisher(self):
        msg=Twist()
        msg.linear.x=0.1
        msg.angular.z=0.0
        self.pub.publish(msg)
        
    #터틀위치Topic구독
    def subcallback(self, pose):#x,y,theta
        if self.cur_x==0:
            self.cur_x=round(float(pose.x),1)
            print(f'cur_x:{self.cur_x}')
            self.target_x=self.cur_x+self.step
            print(f'target_x:{self.target_x}')
            
        if self.target_x==round(float(pose.x),1):
            self.target_x+=self.step
            print(f'target_x:{self.target_x}')
            
        # print(f'cur_x={round(float(pose.x),1)}')
        # print(f'pose.x:{pose.x},pose.y:{pose.y},pose.theta:{pose.theta}')
        # self.get_logger().info(f'pose.x:{pose.x},pose.y:{pose.y},pose.theta:{pose.theta}')


def main():
    rclpy.init()
    node=Message_Publisher()
        
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('KeyboardInterrupt Error')
    finally:
        node.destroy_node
        rclpy.shutdown()
    print('Exit the Program')

if __name__=='__main__':
    main()