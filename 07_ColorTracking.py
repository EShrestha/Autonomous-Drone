from djitellopy import tello
import cv2 
import numpy as np

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()
drone.takeoff()
drone.send_rc_control(0, 0, 0, 0)

low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])

while True:
    
    frame = drone.get_frame_read().frame
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green_mask = cv2.GaussianBlur(green_mask,(5,5),100) 

    cv2.imshow("ColorTracking", frame)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    percent_green = (np.sum(green_mask) / np.size(green_mask)/255) * 100
    print(percent_green)
    cv2.waitKey(1)

    #lets say 10 is the perfect distance
    #only problem is when somewhat far away is the same percentages 
    # as when basically the person is not even there
    # might need to do some kind of area equation to make sure the green isn't scattered around the screen
    #and rather a big block or chunk
    
    #also prob want to remove noise in frames
    #prob cv2.contourArea()

    #psuedo code
    #if(detectGreen):
        #if(percent_green < 10):
            #moveForward
        #elif(percent_green > 12):
            #moveBackward
        #otherwise dont move at all
    #else
        #keeps turning in circles until you detect green 