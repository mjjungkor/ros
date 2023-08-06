import rclpy
from rclpy.node import Node
from mj_interfaces.msg import ArithmeticArgument

class Argument(Node):
    def __init__(self):
        super().__init__('argument')
        self.pub=self.create_publisher(ArithmeticArgument, 'arithmetic_argument', 10)        
        self.timer=self.create_timer(1,self.publishers)

    def publishers(self):
        msg=ArithmeticArgument()
        msg.stamp=self.get_clock().now().to_msg()
        msg.argument_a=3.0
        msg.argument_b=5.0
        self.pub.publish(msg)


def main():
    rclpy.init()
    node=Argument()
        
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