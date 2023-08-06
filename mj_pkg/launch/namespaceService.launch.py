from launch import LaunchDescription
from launch_ros.actions import Node

# def generate_launch_description():#namespace적용
#     #node_executable 명령어
#     return LaunchDescription([
#         Node(package='mj_pkg',namespace='/j',node_executable='simplesss',output='screen')
#         ]
#         )

from launch.actions import DeclareLaunchArgument
import os

def generate_launch_description():#DeclareLaunchArgument를 사용하여 한번에 적용
    return LaunchDescription([
        DeclareLaunchArgument('ros_namespace',default_value=os.environ['ROS_NAMESPACE']),
        Node(package='mj_pkg',executable='simplesss',output='screen')
        ]
        )