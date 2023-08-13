import rclpy
import random
from rclpy.node import Node
from mj_interfaces.msg import ArithmeticArgument
from rcl_interfaces.msg import SetParametersResult

class Argument(Node):
    def __init__(self):
        super().__init__('argument')
        self.declare_parameter('min_random_num',0) #외부로부터 사용될 변수, '0'은 default value
        self.min_random_num = self.get_parameter('min_random_num').value #클래스 내부에서 사용할 변수
        self.declare_parameter('max_random_num',7)
        self.max_random_num = self.get_parameter('max_random_num').value
        self.add_on_set_parameters_callback(self.update_parameter) #생성될때 최초 1회가 아닌 실행중에도 들어오는 값을 처리하기 위한 서비스
        self.pub=self.create_publisher(ArithmeticArgument, 'arithmetic_argument', 10)        
        self.timer=self.create_timer(1,self.publishers)

    def publishers(self):
        msg=ArithmeticArgument()
        msg.stamp=self.get_clock().now().to_msg()
        msg.argument_a=float(random.randint(self.min_random_num, self.max_random_num))
        msg.argument_b=float(random.randint(self.min_random_num, self.max_random_num))
        #print(f'msg.argument_a:{msg.argument_a},msg.argument_b:{msg.argument_b}')
        self.get_logger().info(f'msg.argument_a:{msg.argument_a},msg.argument_b:{msg.argument_b}')
        self.pub.publish(msg)

    def update_parameter(self, params):
        for param in params:
            if param.name == 'min_random_num':
                self.min_random_num=param.value
            if param.name == 'max_random_num':
                self.max_random_num=param.value
        
        return SetParametersResult(successful=True)
            


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