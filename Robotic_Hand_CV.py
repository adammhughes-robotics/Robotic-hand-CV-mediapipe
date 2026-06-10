import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
import math
import socket #used to send Data to unity/ROS2

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('127.0.0.1', 5051)) # Sends to Linux (WSL) ROS2
#Function to get joint angle 
import numpy as np



##########################
def DOT_prod(x,y,z,):
  
 # SQ1 = math.sqrt(x**2 + y**2 + z**2)
  Theta=math.acos(y / (math.sqrt((x*x + y*y + z*z))))
  return Theta


def angle_sideways(x1, y1, z1, x2, y2, z2):
    x= x2 - x1
    y= y2 - y1
    z= z2 - z1
   
    
    angle=math.acos(x / (math.sqrt((x*x + y*y + z*z))))
    if 1.5<angle :
        angle = 1.5
    elif  angle > 2.2:
        angle = 2.2
    else:
       angle = angle
    

    return  angle
# Testing a new function -> trying to get thumb more accurate
def angle_at_joint_test(x1, y1, z1, x2, y2, z2):
    # This is used for the Thumb
    x= x2 - x1
    y= y2 - y1
    z= z2 - z1
   
    #I will do dot product to get the angle
    V=math.sqrt(x**2 + y**2 + z**2)
    # assuming the ideal case
    send_Angle = math.acos(x / V) if V != 0 else 0

    return  send_Angle
    
  
#-------------------------------------------------------------------------------------------
arrX = []
arrY = []
arrZ = []
def my_hand_function(ArrX, ArrY, ArrZ):
  data_angles = [] # this is the list of all angles in the hand 
  print("==================================")
  
  if  ArrX[5] < ArrX[17] :
    print("RIGHT HAND  \n\n")

  else :
    print("LEFT HAND \n\n ")
  print("==================================")
  
  #print("The coordinates of pointer finger of the hand are: ")

  # Thumb displacements (landmark to landmark)
  Y_dis_0_1 = ArrY[1] - ArrY[0]   # wrist → CMC
  Z_dis_0_1 = ArrZ[1] - ArrZ[0]
  X_dis0_1 = ArrX[1] - ArrX[0]

  Y_dis_1_2 = ArrY[2] - ArrY[1]   # CMC → MCP
  Z_dis_1_2 = ArrZ[2] - ArrZ[1]
  X_dis1_2 = ArrX[2] - ArrX[1]

  Y_dis_2_3 = ArrY[3] - ArrY[2]   # MCP → IP
  Z_dis_2_3 = ArrZ[3] - ArrZ[2]
  X_dis2_3 = ArrX[3] - ArrX[2]

  Y_dis_3_4 = ArrY[4] - ArrY[3]   # IP → TIP
  Z_dis_3_4 = ArrZ[4] - ArrZ[3]
  X_dis3_4 = ArrX[4] - ArrX[3]

  #starting from land mark zero then 5 to 8
  #X_displacement_relative to landmark 0
  X_dis05= ArrX[5] - ArrX[0]
  
  #for y displacement
  Y_dis05= ArrY[5] - ArrY[0]
  # for z displacement
  Z_dis05= ArrZ[5] - ArrZ[0]
  
  #6 relative to 5
  X_dis56= ArrX[6] - ArrX[5]
  #for y displacement
  Y_dis56= ArrY[6] - ArrY[5]
  # for z displacement
  Z_dis56= ArrZ[6] - ArrZ[5]
  
  #7 relative to 6
  X_dis67= ArrX[7] - ArrX[6]
  #for y displacement
  Y_dis67= ArrY[7] - ArrY[6]
  # for z displacement
  Z_dis67= ArrZ[7] - ArrZ[6]
  
  #8 relative to 7
  X_dis78= ArrX[8] - ArrX[7]
  #for y displacement
  Y_dis78= ArrY[8] - ArrY[7]
  # for z displacement
  Z_dis78= ArrZ[8] - ArrZ[7]
  #print("X_displacement_relative to 0 is ", X_dis05)
  #print("Y_displacement_relative to 0 is ", Y_dis05)  
  #print("Z_displacement_relative to 0 is ", Z_dis05)
  #print("X_displacement_relative to 5 is ", X_dis56)
  #print("Y_displacement_relative to 5 is ", Y_dis56)  
  #print("Z_displacement_relative to 5 is ", Z_dis56)
  #print("X_displacement_relative to 6 is ", X_dis67)
  #print("Y_displacement_relative to 6 is ", Y_dis67)  
  #print("Z_displacement_relative to 6 is ", Z_dis67)
  #print("X_displacement_relative to 7 is ", X_dis78)
  #print("Y_displacement_relative to 7 is ", Y_dis78)  
  #print("Z_displacement_relative to 7 is ", Z_dis78)
  #---------------------------------------------------------------------------

# middle finger is 9 to 12
  X_dis_9_10= ArrX[10] - ArrX[9]
  Y_dis_9_10= ArrY[10] - ArrY[9]
  Z_dis_9_10= ArrZ[10] - ArrZ[9]
  
  X_dis_10_11= ArrX[11] - ArrX[10]
  Y_dis_10_11= ArrY[11] - ArrY[10]
  Z_dis_10_11= ArrZ[11] - ArrZ[10]

  X_dis_11_12= ArrX[12] - ArrX[11]
  Y_dis_11_12= ArrY[12] - ArrY[11]
  Z_dis_11_12= ArrZ[12] - ArrZ[11]

# ring finger is 13 to 16
  X_dis_13_14= ArrX[14] - ArrX[13]
  Y_dis_13_14= ArrY[14] - ArrY[13]
  Z_dis_13_14= ArrZ[14] - ArrZ[13]

  X_dis_14_15= ArrX[15] - ArrX[14]
  Y_dis_14_15= ArrY[15] - ArrY[14]
  Z_dis_14_15= ArrZ[15] - ArrZ[14]

  X_dis_15_16= ArrX[16] - ArrX[15]
  Y_dis_15_16= ArrY[16] - ArrY[15]
  Z_dis_15_16= ArrZ[16] - ArrZ[15]

# pinky finger is 17 to 20
  X_dis_17_18= ArrX[18] - ArrX[17]
  Y_dis_17_18= ArrY[18] - ArrY[17]
  Z_dis_17_18= ArrZ[18] - ArrZ[17]

  X_dis_18_19= ArrX[19] - ArrX[18]
  Y_dis_18_19= ArrY[19] - ArrY[18]
  Z_dis_18_19= ArrZ[19] - ArrZ[18]
  
  X_dis_19_20= ArrX[20] - ArrX[19]
  Y_dis_19_20= ArrY[20] - ArrY[19]
  Z_dis_19_20= ArrZ[20] - ArrZ[19]



# all points for pointer finger

  #print("x=[", ArrX[0],",",ArrX[5],",",ArrX[6],",",ArrX[7],",",ArrX[8],"]")
  #print("y=[", ArrY[0],",",ArrY[5],",",ArrY[6],",",ArrY[7],",",ArrY[8],"]")
  #print("z=[", ArrZ[0],",",ArrZ[5],",",ArrZ[6],",",ArrZ[7],",",ArrZ[8],"]")
#_______________________________________________________________________
  #ANGLE OF THE JOINTS SOH CAH TOA

  # Calculate angles for each joint using Z and Y displacements
  #USING ARC TAN TO CALCULATE THE ANGLE OF THE JOINTS
  # Assuminng ideal case
  # angle of the pam
  #angle0 = math.atan2((Y_dis05) ,(Z_dis05))
  angle0=DOT_prod(X_dis05,Y_dis05,Z_dis05) # this is the angle of the pam in radians
  data_angles.append(angle0) #Add the angle of the pam to the list of angles to send to unity and ros2
# Thumb is 1 to 4
  
  angle_thumb_0_1 = angle_at_joint_test( ArrX[1], ArrY[1], ArrZ[1],ArrX[0], ArrY[0], ArrZ[0]) # this is the angle of joint 1 in radians to send to unity and ros2
  #angle_thumb_cmc = math.atan2(Y_dis_0_1, Z_dis_0_1) - angle0  # [1]
  angle_thumb_1_2 = angle_at_joint_test( ArrX[2], ArrY[2], ArrZ[2],ArrX[0], ArrY[0], ArrZ[0],) # this is the angle of joint 1 in radians to send to unity and ros2
  # angle_thumb_mcp = math.atan2(Y_dis_1_2, Z_dis_1_2) - angle0  # [2]
  #angle_thumb_2_3_Yaw = angle_at_joint_test(ArrX[1])#math.atan2(Y_dis_2_3, X_dis2_3) # [3]
  angle_thumb_2_3  =angle_at_joint_test( ArrX[3], ArrY[3], ArrZ[3],ArrX[2], ArrY[2], ArrZ[2]) #math.atan2(Y_dis_2_3, Z_dis_2_3) - angle0  # [3]
  angle_thumb_3_4 =angle_at_joint_test(  ArrX[4], ArrY[4], ArrZ[4],ArrX[3], ArrY[3], ArrZ[3] )# tip joint of thumb
  
  
  
  data_angles.append(angle_thumb_1_2) # index 1
  data_angles.append(angle_thumb_2_3)   # index 2
  #data_angles.append(-math.radians(angle_thumb3)) 
  data_angles.append(angle_thumb_3_4)   # index 3

#   print(f"Thumb 1_2 angle:  {angle_thumb_1_2:.1f}°")
#   print(math.radians(angle_thumb_1_2)-angle0)
#   print(f"Thumb MCP angle:  { angle_thumb_2_3:.1f}°")
#   print(math.radians(angle_thumb_2_3)-angle0)
#   print(f"Thumb IP  angle:  {angle_thumb_3_4:.1f}°")
#   print(math.radians(angle_thumb_3_4)-angle0)
  
  
  
  #for pointer finger
  
  test_Angle = 90
# NEED TO LOOK INTO THIS  MORE might need to be negative rather thatn positive.
  #if(Y_dis05<0 and Y_dis56 <0 and Y_dis67 <0 and Y_dis78 <0): # if all joints are higher than the previous joint. scince then top of the camera is zero and the bottom is positive. so if all joints are higher than the previous joint, then the angles should be negative.
  #angle5 = (math.atan2(Y_dis56,Z_dis56))-angle0
  angle5 = DOT_prod(X_dis56,Y_dis56,Z_dis56)-angle0
  data_angles.append(angle5) # 4this is the angle of joint 5 in radians to send to unity and ros2

  #angle6 = (math.atan2(Y_dis67 , Z_dis67))-angle0#+(90-angle5) # to get angle of missing joint to get relative to point 5
  angle6 = DOT_prod(X_dis67,Y_dis67,Z_dis67)-angle0
  data_angles.append(angle6) # 5:this is the angle of joint 6 in radians to send to unity and ros2
  
  #angle7 = (math.atan2(Y_dis78,Z_dis78))-90
  angle7 = DOT_prod(X_dis78,Y_dis78,Z_dis78)-angle0
  data_angles.append(angle7) #6: this is the angle of joint 7 in radians to send to unity and ros2
  
  
  #angle9 = (math.atan2(Y_dis_9_10,Z_dis_9_10))-angle0
  angle9 = DOT_prod(X_dis_9_10,Y_dis_9_10,Z_dis_9_10)-angle0
  data_angles.append(angle9) #7: this is the angle of joint 9 in radians to send to unity and ros2
    

  #angle10 = (math.atan2(Y_dis_10_11,Z_dis_10_11))-angle0
  angle10 = DOT_prod(X_dis_10_11,Y_dis_10_11,Z_dis_10_11)-angle0
  data_angles.append(angle10) #8: this is the angle of joint 10 in radians to send to unity and ros2
  
  
  #angle11 = (math.atan2(Y_dis_11_12,Z_dis_11_12))-90
  angle11 = DOT_prod(X_dis_11_12,Y_dis_11_12,Z_dis_11_12)-angle0
  data_angles.append(angle11) #9: this is the angle of joint 11 in radians to send to unity and ros2
      
 
  #angle13 = (math.atan2(Y_dis_13_14,Z_dis_13_14))-angle0 
  angle13 = DOT_prod(X_dis_13_14,Y_dis_13_14,Z_dis_13_14)-angle0
  data_angles.append(angle13) #10: this is the angle of joint 13 in radians to send to unity and ros2
  
  
  #angle14 = (math.atan2(Y_dis_14_15,Z_dis_14_15))-angle0
  angle14 = DOT_prod(X_dis_14_15,Y_dis_14_15,Z_dis_14_15)-angle0
  data_angles.append(angle14) #11: this is the angle of joint 14 in radians to send to unity and ros2
  
  
  #angle15 = (math.atan2(Y_dis_15_16,Z_dis_15_16))-angle0
  angle15 = DOT_prod(X_dis_15_16,Y_dis_15_16,Z_dis_15_16)-angle0
  data_angles.append(angle15) #12: this is the angle of joint 15 in radians to send to unity and ros2
  
  
  #angle17 = (math.atan2(Y_dis_17_18,Z_dis_17_18))-angle0 
  angle17 = DOT_prod(X_dis_17_18,Y_dis_17_18,Z_dis_17_18)-angle0
  data_angles.append(angle17) #13: this is the angle of joint 17 in radians to send to unity and ros2
  
  
  #angle18 = (math.atan2(Y_dis_18_19,Z_dis_18_19))-angle0
  angle18 = DOT_prod(X_dis_18_19,Y_dis_18_19,Z_dis_18_19)-angle0
  data_angles.append(angle18) #14: this is the angle of joint 18 in radians to send to unity and ros2
  
  
  #angle19 = (math.atan2(Y_dis_19_20,Z_dis_19_20))-angle0
  angle19 = DOT_prod(X_dis_19_20,Y_dis_19_20,Z_dis_19_20)-angle0
  data_angles.append(angle19) #15: this is the angle of joint 19 in radians to send to unity and ros2
  
  
  #data_angles.append(angle_thumb_2_3_Yaw)   # index 3 for yaw of thumb
  data_angles.append(angle_thumb_0_1- math.radians(90)) #(16) this is the angle of the thumb in radians to send to unity and ros2
  data_angles.append(angle_sideways(ArrX[5], ArrY[5], ArrZ[6], ArrX[6], ArrY[6], ArrZ[6])-math.radians(90)) #(17) this is the angle of the hand in radians to send to unity and ros2
  data_angles.append(angle_sideways(ArrX[9], ArrY[9], ArrZ[9], ArrX[10], ArrY[10], ArrZ[10])-math.radians(90)) #(18) this is the angle of the hand in radians to send to unity and ros2
  data_angles.append(angle_sideways(ArrX[13], ArrY[13], ArrZ[13], ArrX[14], ArrY[14], ArrZ[14])-math.radians(90)) #(19) this is the angle of the hand in radians to send to unity and ros2
  data_angles.append(angle_sideways(ArrX[17], ArrY[17], ArrZ[17], ArrX[18], ArrY[18], ArrZ[18])-math.radians(90)) #(20) this is the angle of the hand in radians to send to unity and ros2
  #--------------------------------------------------------------------------------------------------------------------
  # ANGLELS PRINT DATA STUFF
  # --------------------------------------------------------------------------------------------------------------------

  #print("GENERAL HANND ANGLE  (05) Angle at joint 0 is ", math.degrees(angle0))

#   print("(56) Angle at joint 5 is ", math.degrees(angle5)-test_Angle) # to get angle of missing joint to get relative to point 0
#   print("(67) Angle at joint 6 is ", math.degrees(angle6)-test_Angle)
#   print("(78) Angle at joint 7 is ", math.degrees(angle7)-test_Angle)
#   print("(9_10) Angle at joint 9 is ", math.degrees(angle9)-test_Angle)
#   print("(10_11) Angle at joint 10 is ", math.degrees(angle10)-test_Angle)
#   print("(11_12) Angle at joint 11 is ", math.degrees(angle11)-test_Angle  )
#   print("(13_14) Angle at joint 13 is ", math.degrees(angle13)-test_Angle)
#   print("(14_15) Angle at joint 14 is ", math.degrees(angle14)-test_Angle)
#   print("(15_16) Angle at joint 15 is ", math.degrees(angle15)-test_Angle)
#   print("(17_18) Angle at joint 17 is ", math.degrees(angle17)-test_Angle)
#   print("(18_19) Angle at joint 18 is ", math.degrees(angle18)-test_Angle)
#   print("(19_20) Angle at joint 19 is ", math.degrees(angle19)-test_Angle)



  
  
  #--------------------------------------------------------------------------------------------------------------------
  # this is the data that will be sent to ros2
#   print("#############==================================")
#   print("Data angles = ", data_angles)  # Print the list of angles to send to unity and ros2
  # SENDING DATA TO ROS2 joint state publisher
  server.send(str.encode(str(data_angles))) # this is the list of all coordinates of the

  
#_______________________________________________________________________

#AGLE OF THE JOINTS SOH CAH TOA

  ArrX.clear()
  ArrY.clear()
  ArrZ.clear()
#-------------------------------------------------------------------------------------------



# For webcam input:
width, height = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, width)#for unity 
cap.set(4, height)#fot unnity
# TESTING UNITY COMMUNivation from this code...
#sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#serverAddressPort = ("127.0.0.1", 5051) # PLACE HOLDER -->>>>IP and Port of the Unity Server 



#SIDE NOTE LOOK INTO ->>>>> Gimbal lock  ->  Work with matrixcies



with mp_hands.Hands(
    min_detection_confidence=0.9,
    min_tracking_confidence=0.9) as hands:
  

  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)
    image_height, image_width, _ = image.shape
    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    data=[]

    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        # Here is How to Get All the Coordinates
        for ids, landmrk in enumerate(hand_landmarks.landmark):
            # print(ids, landmrk)
            cx, cy, cz = landmrk.x , landmrk.y, landmrk.z
            arrX.append(cx)
            arrY.append(height - cy)
            arrZ.append(cz)
            #print(cx, cy)
            #print (ids, cx, cy, cz)
            data.extend([cx*width,height-(cy*height), cz]) # this is the list of all coordinates of the hand in the format [x0, y0, z0, x1, y1, z1, ..., x20, y20, z20]


        #lmList = hand["lmList"]  # List of 21 Landmark points
        #print(lmList)
        #for lm in lmList:
            #data.extend([   lm[0], height -lm[1], lm[2] ])  # x, y, z coordinates of each landmark
            # the reason we take height - lm[1] is because in computer vision, the y-coordinate increases downwards, but in Unity, it increases upwards. So we need to invert the y-coordinate to match Unity's coordinate system.    
        
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        print("------------------------------" )
#-------------------------------------------------------------------------------------------
      # unity communication CODE
      print("Data = ", data)  # Print the list of coordinates 
      # Send data to Unity
      #sock.sendto(str.encode(str(data_angles)), serverAddressPort)
      

      my_hand_function(arrX, arrY, arrZ) # call my function


      #print("y=[", arrY[0],",",arrY[5],",",arrY[6],",",arrY[7],",",arrY[8],"]")
      #print("z=[", arrZ[0],",",arrZ[5],",",arrZ[6],",",arrZ[7],",",arrZ[8],"]")


      
      # Clears the arrays before the next loop to store new coordinates
      arrX.clear()
      arrY.clear()
      arrZ.clear()
#-------------------------------------------------------------------------------------------

    cv2.imshow('MediaPipe Hands', image)
    
    if cv2.waitKey(1) & 0xFF == 27:
      break
cap.release()

