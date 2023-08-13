from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():#DeclareLaunchArgument를 사용하여 한번에 적용
    #param_dir=/home/mjjung/colcon_ws/install/arithmetic_ex/share/arithmetic_ex/param/argument.yaml
    param_dir=LaunchConfiguration(
        'param_dir',
        default=os.path.join(get_package_share_directory('arithmetic_ex'),'param','argument.yaml'))
    return LaunchDescription([
        DeclareLaunchArgument(
            'param_dir',
            default_value=param_dir,
            description='full path of parameter file'),#노드별 추가가 아닌 한번에 추가하기 위해서
        Node(package='arithmetic_ex',executable='argument',#topic publisher
             parameters=[{'min_random_num':10,'max_random_num':50}], #launch
             #parameters=[param_dir], #yaml
             output='screen'),
        Node(package='arithmetic_ex',executable='argumentsub',#topic subscribe
             parameters=[{'min_random_num':10,'max_random_num':50}], #launch
             #parameters=[param_dir], #yaml
             output='screen')
        ]
        )