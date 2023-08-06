import rclpy
import random
from rclpy.node import Node
from mj_interfaces.srv import TwoIntAdd

class Simple_service_client(Node):
    def __init__(self):
        super().__init__('twonumber_cli')
        self.client=self.create_client(TwoIntAdd,'mj_addtwoint')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.msg=TwoIntAdd.Request()
        
    def call_service(self):        
        self.msg.a_number=random.randint(0,200)
        self.msg.b_number=random.randint(0,200)
        
        self.future=self.client.call_async(self.msg)#TCP
        rclpy.spin_until_future_complete(self,self.future)
        return self.future.result()



def main():
    rclpy.init()
    node=Simple_service_client()

    try:
        #rclpy.spin(node)
        response=node.call_service()#1회
        node.get_logger().info(f'Received message:{response.return_number}')
        #주기적으로 호출(타이머사용필요)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()