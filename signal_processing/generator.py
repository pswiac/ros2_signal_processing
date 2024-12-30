import rclpy
from rclpy.node import Node
import math
from std_msgs.msg import String, Float64


class SignalPublisher(Node):

    def __init__(self):
        super().__init__('generator')
        self.declare_parameter('amplitude', rclpy.Parameter.Type.INTEGER)  
        self.declare_parameter('frequency', rclpy.Parameter.Type.INTEGER) 

        self.publisher_ = self.create_publisher(Float64, 'signal', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        amp = self.get_parameter('amplitude')
        fr = self.get_parameter('frequency')

        sine_wave = Float64()
        sine_wave.data = amp.value * math.sin(2*math.pi*fr.value*self.i/100.0)
        self.publisher_.publish(sine_wave)
        self.get_logger().info(f'Publishing: "{sine_wave.data} - freq: {fr.value} - amp: {amp.value}"')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    signal_publisher = SignalPublisher()

    rclpy.spin(signal_publisher)

    signal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
