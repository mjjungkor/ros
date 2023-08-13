import rclpy
from rclpy.node import Node
from mj_interfaces.msg import ArithmeticArgument

class Argument_Sub(Node):
    def __init__(self):
        super().__init__('argument_sub')
        #DDS에는 string type이 없어 'from std_msgs.msg import String' 진행
        #10은 메시지를 받을 buffer의 크기
        self.create_subscription(ArithmeticArgument, 'arithmetic_argument', self.subcallback, 10)        
        

    def subcallback(self, msg):
        #print(msg.data)
        self.get_logger().info(f'Received Time : {msg.stamp.sec},{msg.stamp.nanosec}')
        self.get_logger().info(f'Received Message : {msg.argument_a},{msg.argument_b}')#시간/출처(노드이름) 정보 자동 추가
        #self.get_logger().error(msg.data)


def main():
    rclpy.init()
    node=Argument_Sub()
        
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