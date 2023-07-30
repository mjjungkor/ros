import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

MAX_LIN_VEL=0.22
MAX_ANG=2.84

class move_turtle(Node):
    def __init__(self):
        # super().__init__('simple_pub')
        super().__init__('mturtle')
        self.pub=self.create_publisher(Twist, 'turtle1/cmd_vel',10)
        self.pub2=self.create_publisher(Twist, 'turtle2/cmd_vel',10)   
        self.create_timer(0.1,self.publisher)
        self.create_timer(0.1,self.publisher2)
        self.create_timer(1/60,self.update)
        self.dir=1.0
        self.speed=0.0

    def publisher(self):
        msg=Twist()# rqt 'message type browser'에서 세부 내용 확인

        # msg.linear.x=1.0#1m/s 이동
        # msg.linear.y=0.0
        # msg.linear.z=0.0
        # msg.angular.x=0.0
        # msg.angular.y=0.0
        # msg.angular.z=1.0#1radian 60도/s 회전

        msg.linear.x=self.speed
        msg.angular.z=self.dir  
        msg = self.restrain(msg)  
        self.pub.publish(msg)

    def publisher2(self):
        msg=Twist()# rqt 'message type browser'에서 세부 내용 확인

        msg.linear.x=self.speed
        msg.angular.z=-self.dir  
        msg = self.restrain(msg)  
        self.pub2.publish(msg)

    def update(self):
        self.speed+=0.001*self.dir
        if self.speed>2:
            self.dir=-1.0
        elif self.speed<0:
            self.dir=1.0
        # self.dir+=0.02
        # self.speed+=0.02

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
    node=move_turtle()
        
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('KeyboardInterrupt Error')
    finally:
        node.destroy_node
        rclpy.shutdown()
    print('This is test')

if __name__=='__main__':
    main()