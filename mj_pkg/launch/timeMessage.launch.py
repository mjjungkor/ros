from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    #node_executable 명령어
    return LaunchDescription([
        Node(package='mj_pkg',node_executable='simpletimepub',output='screen'),
        Node(package='mj_pkg',node_executable='messagesub1',output='screen'),
        Node(package='mj_pkg',node_executable='messagesub2',output='screen'),
        Node(package='mj_pkg',node_executable='messagetimepub',output='screen'),
        Node(package='mj_pkg',node_executable='messagetimesub',output='screen')]
        )