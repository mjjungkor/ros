#하나의 노드에서 2개의 토픽 발행
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Sim_pub(Node):
    def __init__(self):
        super().__init__('message_pub')#노드이름
        #DDS에는 string type이 없어 'from std_msgs.msg import String' 진행
        #10은 메시지를 받을 buffer의 크기이며 나머지는 기본 값으로 설정
        self.pub=self.create_publisher(String, 'listen_message1',10)      
        self.pub2=self.create_publisher(String, 'listen_message2',10)               
        self.create_timer(1,self.publisher)
        self.create_timer(2,self.publisher2)
        self.count=0

    def publisher(self):
        msg=String()
        msg.data='ros message pub#1 '+str(self.count)
        self.pub.publish(msg)
        #self.pub2publish(msg)
        self.count+=1

    def publisher2(self):
        msg=String()
        msg.data='ros message pub#2 '+str(self.count)
        self.pub2.publish(msg)
        


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
