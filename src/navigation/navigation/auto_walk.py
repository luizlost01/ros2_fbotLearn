#!/usr/bin/env python3

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

        self.get_logger().info("Published Walk")

    def scan_callback(self, msg: LaserScan):
        scan_arr = msg.ranges
        # Array do Scan a Direita
        dist_direita = scan_arr[30:90]
        dist_centro = scan_arr[90:180]
        dist_esquerda = scan_arr[180:200]



        #Verifica se algum valor do array a esquerda é menor ou igual a 1.5
        right_obstacle = any(dist <= 0.4 for dist in dist_esquerda)
        #Verifica se algum valor do array a direita é menor ou igual a 1.5
        left_obstacle = any(dist <= 0.4 for dist in dist_direita)
        #Verifica se algum valor do array ao centro é menor ou igual a 1.5
        center_obstacle = any(dist <= 0.4 for dist in dist_centro)

        #Chama a função Publish_walk
        self.publish_walk(right_obstacle, left_obstacle, center_obstacle)

    def odom_callback(self, msg: Odometry):
        robotPos_x = msg.pose.pose.position.x
        robotPos_y = msg.pose.pose.position.y

        self.robotPos = robotPos_x, robotPos_y


    #Função de andar
    def publish_walk(self, right_obstacle, left_obstacle, center_obstacle):
        msg = Twist()
        goalPos = (5,4)


        goal = math.dist(goalPos, self.robotPos)

        vel_x = 0.5
        ang_z = 0.25
        
        if center_obstacle:
            msg.angular.z = -0.2
            self.publisher.publish(msg)
        elif not center_obstacle:
            msg.linear.x = 0.2
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