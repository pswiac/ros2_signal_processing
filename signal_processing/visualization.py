import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Float64


class ToolSubscriber(Node):

    def __init__(self):
        super().__init__('visualization')
        #print("init for subscriber")


        self.subscription = self.create_subscription(
            Float64,
            'modified_signal',
            self.modified_callback,
            10)
        
        self.subscription = self.create_subscription(
            Float64,
            'signal',
            self.original_callback,
            10
        )

    def modified_callback(self, msg):
        self.get_logger().info(f'Modified Signal: "{msg.data}"')


    def original_callback(self, msg):
        self.get_logger().info(f'Original Signal: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)

    signal_subscriber = ToolSubscriber()

    rclpy.spin(signal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    signal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()