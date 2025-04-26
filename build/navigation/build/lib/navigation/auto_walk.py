#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Publisher(Node):
    def __init__(self):
        super().__init__("publisher")

        self.subscription = self.create_subscription(LaserScan, "/base_scan", self.scan_callback, 10)        
        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)

        self.get_logger().info("Published Walk")

    def scan_callback(self, msg: LaserScan):
        scan_arr = msg.ranges
        # Array do Scan a Direita
        dist_direita = scan_arr[0:90]
        dist_esquerda = scan_arr[100:240]


        #Verifica se algum valor do array a esquerda é menor ou igual a 2
        right_obstacle = any(dist <= 1.5 for dist in dist_esquerda)
        #Verifica se algum valor do array a direita é menor ou igual a 2
        left_obstacle = any(dist <= 1.5 for dist in dist_direita)

        self.publish_walk(right_obstacle, left_obstacle)
        
    #Função de andar
    def publish_walk(self, right_obstacle, left_obstacle):
        msg = Twist()
        vel_x = 0.4
        if (left_obstacle and right_obstacle == False):
            msg.linear.x = vel_x
            msg.angular.z = 0.0
            self.publisher.publish(msg)
        elif(left_obstacle == True):
            msg.linear.x = vel_x
            msg.angular.z = 0.5
            self.publisher.publish(msg)
        elif(right_obstacle == True):
            msg.linear.x = vel_x
            msg.angular.z = -0.5
            self.publisher.publish(msg)
        else:
            msg.linear.x = vel_x
            msg.angular.z = 0.0
            self.publisher.publish(msg)
        print(left_obstacle, right_obstacle)

def main(args=None):
    rclpy.init(args=None)
    node = Publisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()