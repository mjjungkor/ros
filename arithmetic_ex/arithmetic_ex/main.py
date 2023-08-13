import rclpy
from rclpy.node import Node
from mj_interfaces.msg import ArithmeticArgument
from mj_interfaces.srv import ArithmeticOperator
from mj_interfaces.action import ArithmeticChecker
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.action import ActionServer
import time

class Calcurator(Node):
    def __init__(self):
        super().__init__('calculator')
        #DDS에는 string type이 없어 'from std_msgs.msg import String' 진행
        #10은 메시지를 받을 buffer의 크기
        self.create_subscription(ArithmeticArgument, 'arithmetic_argument', self.subcallback, 10)
        #콜백그룹(ReentrantCallbackGroup) 서버가 2개 이상이 동시에 운영되면 블락이 생기기때문에 스레드처럼 사용 가능한 기능       
        self.create_service(ArithmeticOperator,
                            'arithmetic_operator', 
                            self.get_arithmetic_operator,callback_group=ReentrantCallbackGroup()) 
        self.arithmetic_action_server=ActionServer(self,ArithmeticChecker,'arithmetic_checker',
                                                   self.executor_callback,callback_group=ReentrantCallbackGroup())
        self.argument_a=0.0
        self.argument_b=0.0
        self.arithmetic_result=0.0
        self.argument_result=0.0
        self.argument_formula=''
        self.argument_symbol=['+','-','*','/']
        self.argument_operator = 1


    def subcallback(self, msg):
        #print(msg.data)
        self.get_logger().info(f'Received Time : {msg.stamp.sec},{msg.stamp.nanosec}')
        self.get_logger().info(f'Received Message : {msg.argument_a},{msg.argument_b}')#시간/출처(노드이름) 정보 자동 추가
        self.argument_b=msg.argument_b
        self.argument_a=msg.argument_a    
        
        if self.argument_operator == ArithmeticOperator.Request.PLUS:
            self.arithmetic_result=self.argument_a+self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.MINUS:
            self.arithmetic_result=self.argument_a-self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.MULTIPLY:
            self.arithmetic_result=self.argument_a*self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.DIVISION:
            if self.argument_b ==0:
                self.arithmetic_result=0.0
            else:
                self.arithmetic_result=self.argument_a/self.argument_b
        self.argument_formula=f'{self.argument_a} {self.argument_symbol[self.argument_operator-1] } {self.argument_b} = {self.arithmetic_result}'
        self.argument_result=self.arithmetic_result
        #self.get_logger().error(msg.data)

    #service
    def get_arithmetic_operator(self, request, response):#request,response는 정해진 변수이름은 아님
        self.argument_operator=request.arithmetic_operator
        if self.argument_operator == ArithmeticOperator.Request.PLUS:
            self.arithmetic_result=self.argument_a+self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.MINUS:
            self.arithmetic_result=self.argument_a-self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.MULTIPLY:
            self.arithmetic_result=self.argument_a*self.argument_b
        if self.argument_operator == ArithmeticOperator.Request.DIVISION:
            if self.argument_b ==0:
                self.arithmetic_result=0.0
            else:
                self.arithmetic_result=self.argument_a/self.argument_b
        self.get_logger().info(f'Receive Servie : {self.argument_operator}')
        response.arithmetic_result=self.arithmetic_result
        return response
    
    def executor_callback(self,goal_handle):
        feedback=ArithmeticChecker.Feedback()
        feedback.formula=[]
        total_sum=0.0
        goal_sum=goal_handle.request.goal_sum
        while total_sum < goal_sum:
            total_sum+=self.argument_result
            feedback.formula.append(self.argument_formula)
            goal_handle.publish_feedback(feedback)
            time.sleep(1)
        goal_handle.succeed()
        result=ArithmeticChecker.Result()
        result.all_formula=feedback.formula
        result.total_sum=total_sum
        return result


def main():
    rclpy.init()
    node=Calcurator()
    executor=MultiThreadedExecutor(num_threads=4)
    executor.add_node(node)
        
    try:
        executor.spin()
    except KeyboardInterrupt:
        print('KeyboardInterrupt Error')
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.shutdown()
    print('This is test')

if __name__=='__main__':
    main()