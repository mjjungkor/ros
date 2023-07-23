import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Sim_pub(Node):
    def __init__(self):
        super().__init__('simple_pub')
        #DDS에는 string type이 없어 'from std_msgs.msg import String' 진행
        #10은 메시지를 받을 buffer의 크기
        self.pub=self.create_publisher(String, 'listen_message',10)        
        self.create_timer(1,self.publisher)

    def publisher(self):
        msg=String()
        msg.data='hello ros'
        self.pub.publish(msg)
        


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