import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        # Declare parameters
        self.declare_parameter('v', 0.0)
        self.declare_parameter('d', 0.0)

        # Publish as fast as possible
        self.create_timer(0.01, self.publish_drive)

    def publish_drive(self):
        msg = AckermannDriveStamped()
        v = self.get_parameter('v').value
        d = self.get_parameter('d').value

        self.get_logger().info(f"Publishing: v={v}, d={d}")
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    talker = Talker()
    rclpy.spin(talker)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

