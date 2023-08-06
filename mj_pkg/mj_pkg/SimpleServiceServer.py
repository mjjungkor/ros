import rclpy
from rclpy.node import Node
from mj_interfaces.srv import TwoIntAdd

class Simple_service_server(Node):
    def __init__(self):
        super().__init__('twonumber')
        self.create_service(TwoIntAdd,'mj_addtwoint',self.twonumber_callback)

    def twonumber_callback(self,request, resopnse):
        self.get_logger().info(f'incomming data:{request.a_number},{request.b_number}')
        resopnse.return_number=request.a_number+request.b_number
        return resopnse


def main():
    rclpy.init()
    node=Simple_service_server()

    try:
        rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()