from djitellopy import tello
from time import sleep
import numpy as np
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    noWhite = cv2.bitwise_and(frame, frame, mask=mask)
    percent_noWhite = (np.sum(mask) / np.size(mask)/255) * 100

    if(percent_noWhite) > 12:
        print("Clear percent: ", percent_noWhite)
        # rc_control =  (left/right, forward/backward, up/down, turning(left,right))
        drone.send_rc_control(0, 1, 0, 0) # Goes forward until the clear percent is less than 12%

        pass
    else:
        # Could make it more advance here by turning left and logging the clear percent 
        # then turning right then logging the clear percent then comparing left vs right on the clear percent to choose which direction to turn
        
        drone.send_rc_control(0, 0, 0, 0) # Stand still
        while(percent_noWhite < 18): # More clear percent than 12 to account for the wall in the drones FOV after it turns
            print("Black percent: ", (100-percent_noWhite))
            print("Turning right...")
            drone.send_rc_control(0, 0, 0, 3) # turns until the clear percent is greater than 12%

        drone.send_rc_control(0, 0, 0, 0)  # Stand still




    cv2.imshow("No White", noWhite)

    key = cv2.waitKey(1)
    if key == 27:
        break
