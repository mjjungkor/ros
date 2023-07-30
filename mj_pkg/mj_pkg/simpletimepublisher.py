import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from rclpy.clock import Clock, ClockType#207페이지

class Sim_time_pub(Node):
    def __init__(self):
        super().__init__('simple_time_pub')
        #DDS에는 string type이 없어 'from std_msgs.msg import String' 진행
        #10은 메시지를 받을 buffer의 크기이며 나머지는 기본 값으로 설정
        self.pub=self.create_publisher(Header, 'listen_time',10)      
        self.create_timer(0.1,self.publisher)
        self.id=0
        self.clock=Clock(clock_type=ClockType.SYSTEM_TIME)

    def publisher(self):
        msg=Header()
        # msg.stamp=self.get_clock().now().to_msg()#ROS_TIME
        msg.stamp=self.clock.now().to_msg()
        msg.frame_id=str(self.id)
        self.pub.publish(msg)
        self.id+=1


def main():
    rclpy.init()
    node=Sim_time_pub()
        
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