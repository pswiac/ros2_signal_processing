import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Float64


class SignalSubscriber(Node):

    def __init__(self):
        super().__init__('modifier')
        self.declare_parameters(
            namespace='',
            parameters=[
                ('scale_factor', rclpy.Parameter.Type.INTEGER),
            ]
        )

        self.scaled_data = Float64()

        self.subscription = self.create_subscription(
            Float64,
            'signal',
            self.listener_callback,
            10)
        
        self.publisher_ = self.create_publisher(Float64, 'modified_signal', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):

        self.publisher_.publish(self.scaled_data)
        self.get_logger().info(f'Modified signal: "{self.scaled_data.data}"')
        self.i += 1

    def listener_callback(self, msg):
        scale_factor = self.get_parameter('scale_factor')
        self.get_logger().info(f'I heard: "{msg.data}"')

        self.scaled_data.data = msg.data * scale_factor.value

        


def main(args=None):
    rclpy.init(args=args)

    signal_subscriber = SignalSubscriber()

    rclpy.spin(signal_subscriber)

    
    signal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()