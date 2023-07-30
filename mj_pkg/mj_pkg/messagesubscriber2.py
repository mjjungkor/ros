import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Sim_sub(Node):
    def __init__(self):
        super().__init__('simple_msg_sub2')
        #DDS에는 string type이 없어 'from std_msgs.msg import String' 진행
        #10은 메시지를 받을 buffer의 크기
        self.create_subscription(String, 'listen_message2', self.subcallback, 10)        
        

    def subcallback(self, msg):
        #print(msg.data)
        self.get_logger().info(f'Received Message : {msg.data}')#시간/출처(노드이름) 정보 자동 추가
        #self.get_logger().error(msg.data)


def main():
    rclpy.init()
    node=Sim_sub()
        
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