from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_cpp',  # The package containing the demo_talker
            executable='talker',      # The executable for the demo_talker node
            name='demo_talker',       # Optional: Name for the node
            output='screen',          # Optional: Output log configuration
        )
    ])