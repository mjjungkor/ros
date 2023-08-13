#Service Client

import rclpy
import random
from rclpy.node import Node
from mj_interfaces.srv import ArithmeticOperator

class Operator(Node):
    def __init__(self):
        super().__init__('operator')
        self.client=self.create_client(ArithmeticOperator,'arithmetic_operator')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.msg=ArithmeticOperator.Request()
        
    def call_service(self):        
        self.msg.arithmetic_operator=random.randint(1,4)
        
        self.future=self.client.call_async(self.msg)#TCP
        rclpy.spin_until_future_complete(self,self.future)
        return self.future.result()



def main():
    rclpy.init()
    node=Operator()

    try:
        #rclpy.spin(node)
        while rclpy.ok():#계속 rclpy작동상태확인(shutdown여부확인)
            #rclpy.spin_once(node)#1회
            response=node.call_service()#1회
            node.get_logger().info(f'Received message:{response.arithmetic_result}')
            input('Press Enter for next service call')
        #주기적으로 호출(타이머사용필요)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()