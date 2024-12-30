from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    

    
    generator_config = os.path.join(
        get_package_share_directory('signal_processing'),
        'config',
        'generator_params.yaml'
        )
    
    modifier_config = os.path.join(
        get_package_share_directory('signal_processing'),
        'config',
        'modifier_params.yaml'
        )


    return LaunchDescription(
        [
            Node(
                package='signal_processing',
                executable='generator',
                parameters = [generator_config]
            ),
            Node(
                package='signal_processing',
                executable='modifier',
                parameters = [modifier_config]
            )
        ]
    )