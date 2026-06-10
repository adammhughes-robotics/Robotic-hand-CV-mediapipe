import ast

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster, TransformStamped

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5051))
server.listen(5)


class StatePublisher(Node):
    def __init__(self):
        rclpy.init()
        super().__init__('state_publisher')
        qos_profile = QoSProfile(depth=10)
        self.joint_pub = self.create_publisher(JointState, 'joint_states', qos_profile)
        self.broadcaster = TransformBroadcaster(self, qos=qos_profile)
        self.nodeName = self.get_name()
        self.get_logger().info("{0} started".format(self.nodeName))

        loop_rate = self.create_rate(30)
        #NEW ROBOT STATE FOR HAND
        wrist_pitch_lower=0.0
        wrist_yaw=0.0
        wrist_pitch_upper=0.0

        index_yaw=0.0
        middle_yaw=0.0
        ring_yaw=0.0
        pinky_yaw=0.0
        index_pitch=0.0
        index_knuckle=0.0
        index_tip=0.0
        middle_pitch=0.0
        middle_knuckle=0.0
        middle_tip=0.0
        ring_pitch=0.0
        ring_knuckle=0.0
        ring_tip=0.0
        pinky_pitch=0.0
        pinky_knuckle=0.0
        pinky_tip=0.0
        thumb_yaw=0.0
        thumb_roll=0.0
        thumb_pitch=0.0
        thumb_knuckle=0.0
        thumb_tip=0.0
       

        # message declarations
        joint_state = JointState()
        client, addr = server.accept()
        print('Connected by', addr)
        try:
            while rclpy.ok():
                rclpy.spin_once(self)
                # update joint_state 
                now = self.get_clock().now()
                joint_state.header.stamp = now.to_msg()
                
                joint_state.name = ['wrist_pitch_lower', 'wrist_yaw', 'wrist_pitch_upper', 'thumb_yaw', 'thumb_roll', 'thumb_pitch', 'thumb_knuckle', 'thumb_tip', 'index_yaw', 'index_pitch', 'index_knuckle', 'index_tip', 'middle_yaw', 'middle_pitch', 'middle_knuckle', 'middle_tip', 'ring_yaw', 'ring_pitch', 'ring_knuckle', 'ring_tip', 'pinky_yaw', 'pinky_pitch', 'pinky_knuckle', 'pinky_tip']
                joint_state.position = [wrist_pitch_lower, wrist_yaw, wrist_pitch_upper, thumb_yaw, thumb_roll, thumb_pitch, thumb_knuckle, thumb_tip, index_yaw, index_pitch, index_knuckle, index_tip, middle_yaw, middle_pitch, middle_knuckle, middle_tip, ring_yaw, ring_pitch, ring_knuckle, ring_tip, pinky_yaw, pinky_pitch, pinky_knuckle, pinky_tip]
                # send the joint state and transform
                self.joint_pub.publish(joint_state)
                # Create new robot state
                #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                #my code



                # Im going to take in the Angle array here
                try:
                    data_angle = client.recv(1024)
                    if not data_angle:
                        print("Client disconnected, waiting for new connection...")
                        client, addr = server.accept()
                        print('Reconnected by', addr)
                        continue

                    angles_fingers = ast.literal_eval(data_angle.decode().strip())
                    # angles_fingers  = data_angle.decode().split(',')
                    
                    #print(angles_fingers)




                    #wrist_pitch_lower=angles_fingers[0]   # rotation of the wrist
                    #wrist_pitch_upper=angles_fingers[0] /2   # rotation of the wrist
                    #thumb_abd = angles_fingers[] #(thumb_abd + 0.01)%0.646   # rotation of thumb
                    #thumb =angles_fingers[1] #(thumb_mcp + 0.01)%0.885    # base joint 
                    #thumb_pip =angles_fingers[2] #(thumb_pip + 0.01)%1.885   # middle joint
                    #thumb_dip =angles_fingers[3] #(thumb_dip + 0.01)%1.955                     # tip of the thumb

                    thumb_yaw = angles_fingers[1]  # rotation of thumb
                    thumb_roll = 0  # base joint 
                    thumb_pitch = angles_fingers[16]  # middle joint
                    thumb_knuckle = angles_fingers[2]
                    thumb_tip = angles_fingers[3]  # tip of the thumb

                    index_yaw = angles_fingers[17]#(index_abd + 0.01)%0.646   

                    
                    index_pitch = angles_fingers[4] 
                    
                    index_knuckle = angles_fingers[5]
                                          
                    index_tip = angles_fingers[6]
                    
                    #midle Finger
                    middle_yaw = angles_fingers[18]

                    middle_pitch = angles_fingers[7]
                    
                    middle_knuckle = angles_fingers[8]
                    
                    middle_tip = angles_fingers[9]

                    #ring_abd = (ring_abd + 0.01)%0.646
                    ring_yaw = angles_fingers[19]
                    
                  
                    ring_pitch = angles_fingers[10]
                   
                    ring_knuckle = angles_fingers[11]

                    
                    ring_tip = angles_fingers[12]

                    #pinky_abd = (pinky_abd + 0.01)%0.646
                    pinky_yaw = angles_fingers[20]
                    pinky_pitch = angles_fingers[13]
                    pinky_knuckle = angles_fingers[14]
                    pinky_tip = angles_fingers[15]
                    #This is wheree I will take in the info from mediapipe script and update the state of the joints in robot hand
                    
                except (ValueError, SyntaxError) as e:
                    print(f"Parse error: {e} — skipping frame")
                except ConnectionResetError:
                    print("Connection reset, waiting for new connection...")
                    client, addr = server.accept()
                    print('Reconnected by', addr)

                
                loop_rate.sleep()
        except KeyboardInterrupt:
            pass
def main():

    node = StatePublisher()
if __name__ == '__main__':
    main() 

     


