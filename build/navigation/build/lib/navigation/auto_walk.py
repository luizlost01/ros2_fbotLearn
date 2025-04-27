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
        dist_direita = scan_arr[30:90]
        dist_centro = scan_arr[90:180]
        dist_esquerda = scan_arr[180:200]



        #Verifica se algum valor do array a esquerda é menor ou igual a 1.5
        right_obstacle = any(dist <= 1 for dist in dist_esquerda)
        #Verifica se algum valor do array a direita é menor ou igual a 1.5
        left_obstacle = any(dist <= 1 for dist in dist_direita)
        #Verifica se algum valor do array ao centro é menor ou igual a 1.5
        center_obstacle = any(dist <= 0.9 for dist in dist_centro)


        self.publish_walk(right_obstacle, left_obstacle, center_obstacle)
        
    #Função de andar
    def publish_walk(self, right_obstacle, left_obstacle, center_obstacle):
        msg = Twist()
        vel_x = 0.5
        if left_obstacle and not right_obstacle:
            msg.linear.x = vel_x
            msg.angular.z = 0.30
            self.publisher.publish(msg)
        elif center_obstacle:
            msg.linear.x = -2.0
            msg.angular.z = -1.0
            self.publisher.publish(msg)

        elif left_obstacle:
            msg.linear.x = vel_x
            msg.angular.z = 0.30
            self.publisher.publish(msg)
        elif right_obstacle and not left_obstacle:
            msg.linear.x = vel_x
            msg.angular.z = -0.30
            self.publisher.publish(msg)
        else:
            msg.linear.x = vel_x
            msg.angular.z = 0.0
            self.publisher.publish(msg)
        print(f"esquerda {left_obstacle}, Centro {center_obstacle} ,Direita {right_obstacle}")

def main(args=None):
    rclpy.init(args=None)
    node = Publisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()