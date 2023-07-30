import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile    #rcl(ros client library)
from rclpy.qos import QoSHistoryPolicy, QoSReliabilityPolicy, QoSDurabilityPolicy
from rclpy.qos import qos_profile_sensor_data   #책 111페이지 참고
from std_msgs.msg import String

class Sim_pub(Node):
    def __init__(self):
        # super().__init__('simple_pub')
        super().__init__('t_pub')
        qos_profile=QoSProfile(history=QoSHistoryPolicy.KEEP_ALL,
                               reliability=QoSReliabilityPolicy.RELIABLE,
                               durability=QoSDurabilityPolicy.TRANSIENT_LOCAL)
        #DDS에는 string type이 없어 'from std_msgs.msg import String' 진행
        #10은 메시지를 받을 buffer의 크기이며 나머지는 기본 값으로 설정
        #self.pub=self.create_publisher(String, 'listen_message',10)      
        self.pub=self.create_publisher(String, 'listen_message',qos_profile)   
        #self.pub=self.create_publisher(String, 'listen_message',qos_profile_sensor_data)  
        self.create_timer(1,self.publisher)
        self.count=0

    def publisher(self):
        msg=String()
        msg.data='hello ros'+str(self.count)
        self.pub.publish(msg)
        self.count+=1


def main():
    rclpy.init()
    node=Sim_pub()
        
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


# import rclpy
# from rclpy.node import Node

# def timerTest():
#     print('test')

# def main():
#     rclpy.init()
#     node=Node('test_node')
#     node.create_timer(1, timerTest)
    
#     try:
#         rclpy.spin(node)
#     except KeyboardInterrupt:
#         print('KeyboardInterrupt Error')
#     finally:
#         node.destroy_node
#         rclpy.shutdown()
#     print('This is test')

# if __name__=='__main__':
#     main()