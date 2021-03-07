import cv2 
from djitellopy import tello
import numpy as np

drone = tello.Tello()
drone.connect()
drone.streamon()
drone.takeoff()

#cap = cv2.VideoCapture(0)

while True:
    #_, frame = cap.read()
    _, frame = drone.get_frame_read().frame

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    low_red = np.array([161, 100, 100])
    high_red = np.array([189, 255, 255])
    #low_red = np.array([161, 155, 84])
    #high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    percent_red = (np.sum(red_mask) / np.size(red_mask)/255) * 100
    if(percent_red) > 2.5: 
        print("RED!")
        drone.flip_left()
 

    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    percent_blue = (np.sum(blue_mask) / np.size(blue_mask)/255) * 100
    if(percent_blue) > 2.5: 
        print("BLUE!")
        drone.flip_back()

    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    percent_green = (np.sum(green_mask) / np.size(green_mask)/255) * 100
    if(percent_green) > 2.5: 
        print("GREEN!")
        drone.flip_right()

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    noWhite = cv2.bitwise_and(frame, frame, mask=mask)
    
    
    
    #cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    cv2.imshow("Nothing", noWhite)

    key = cv2.waitKey(1)
    if key == 27:
        break
