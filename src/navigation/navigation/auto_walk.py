import rclpy
import math
from rclpy.node import Node
from example_interfaces.msg import String

from geometry_msgs.msg import Twist, Pose
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

class Publisher(Node):
    def __init__(self):
        super().__init__("publisher")

        self.laserScan_subscription = self.create_subscription(LaserScan, "/base_scan", self.scan_callback, 10)
        self.odom_subscription = self.create_subscription(Odometry, '/ground_truth', self.odom_callback, 10)

        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.robotPosLive = [0,0,0]
        self.yaw = 0

        self.get_logger().info("Published Walk")

    def scan_callback(self, msg: LaserScan):
        scan_arr = msg.ranges
        # Array do Scan a Direita
        dist_direita = scan_arr[30:90]
        dist_centro = scan_arr[90:180]
        dist_esquerda = scan_arr[180:200]



        #Verifica se algum valor do array a esquerda é menor ou igual a 1.5
        right_obstacle = any(dist <= 0.45 for dist in dist_esquerda)
        #Verifica se algum valor do array a direita é menor ou igual a 1.5
        left_obstacle = any(dist <= 0.45 for dist in dist_direita)
        #Verifica se algum valor do array ao centro é menor ou igual a 1.5
        center_obstacle = any(dist <= 0.45 for dist in dist_centro)

        #Chama a função Publish_walk
        self.publish_walk(right_obstacle, left_obstacle, center_obstacle)

    def odom_callback(self, msg: Odometry):
        robotPos_x = msg.pose.pose.position.x
        robotPos_y = msg.pose.pose.position.y
        
        (_, _, self.yaw) = self.euler_from_quaternion(msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z,msg.pose.pose.orientation.w)

        self.robotPosLive = robotPos_x, robotPos_y
        

    def euler_from_quaternion(self,x, y, z, w):

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x, pitch_y, yaw_z # in radians       

    #Função de andar
    def publish_walk(self, right_obstacle, left_obstacle, center_obstacle):
        msg = Twist()
        goalPos = (5,4)
        robotPos = (-7, -7.1)

        theta = math.atan2(goalPos[1] - self.robotPosLive[1], goalPos[0] - self.robotPosLive[0])
        distancia = math.dist((self.robotPosLive[0], self.robotPosLive[1]), goalPos)
        
        vel_x = 0.5*distancia
        ang_zGoal = 1.0*(theta - self.yaw)
        ang_z = 0.25

        if center_obstacle:
            msg.angular.z = ang_z
            self.publisher.publish(msg)
        
        elif not center_obstacle:
            msg.linear.x = vel_x
            msg.angular.z = ang_zGoal
            self.publisher.publish(msg)
        
        elif right_obstacle:
            msg.angular.z = -0.2
            self.publisher.publish(msg)
        
        elif left_obstacle:
            msg.angular.z = 0.2
            self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=None)
    node = Publisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()