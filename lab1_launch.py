import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    lab1_dir = get_package_share_directory('lab1_pkg')

    # Path to the parameter file
    params_file_path = os.path.join(lab1_dir, 'params', 'lab1_params.yaml')

    return LaunchDescription([
        Node(
            package='lab1_pkg',
            executable='talker',
            name='talker',
            output='screen',
            parameters=[params_file_path]
        ),
        Node(
            package='lab1_pkg',
            executable='relay',
            name='relay',
            output='screen'
        )
    ])


