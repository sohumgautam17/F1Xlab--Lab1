import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Define launch arguments for optional parameters
    v_param = DeclareLaunchArgument('v', default_value='0.0', description='Speed parameter for talker node')
    d_param = DeclareLaunchArgument('d', default_value='0.0', description='Steering angle parameter for talker node')

    # Define nodes
    talker_node = Node(
        package='lab1_pkg',
        executable='talker',  # Replace with the actual executable name if different
        name='talker',
        parameters=[{'v': LaunchConfiguration('v')}, {'d': LaunchConfiguration('d')}]
    )

    relay_node = Node(
        package='lab1_pkg',
        executable='relay',  # Replace with the actual executable name if different
        name='relay'
    )

    # Create launch description and add nodes and arguments
    return LaunchDescription([
        v_param,
        d_param,
        talker_node,
        relay_node
    ])

