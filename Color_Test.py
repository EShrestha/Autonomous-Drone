from djitellopy import tello
import cv2
import numpy as np

drone = tello.Tello()
drone.connect()
print(drone.get_battery())


drone.streamon()
#API REFERENCE - https://djitellopy.readthedocs.io/en/latest/tello/#tello
#CV2 can scan for colors, we can use to have it follow

#Testing
#color_boundries = [
#    ([152,251,152], [0,100,0]), #RGB Range for acceptable colors
#]

#for(lower, upper) in color_boundries
#lower_blue = np.array([100,150,0])
#upper_blue = np.array([140,255,255])
lower_yellow = np.array([22,93,0])
upper_yellow = np.array([45,255,255])

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(360,240))

    #Test Stuff
    mask = cv2.inRange(img, lower_yellow, upper_yellow)
    result = cv2.bitwise_and(img,img,mask = mask)              
    #print(mask)
    #print(mask[0])
    #output = cv2.bitwise_and(image, image, mask=mask)

    #output "255 255 255 ... 255 255 255" or "0 0 0 ... 0 0 0"

    cv2.imshow("Drone Image", img)         
    cv2.imshow('result',result)   
    #cv2.imshow(img, cmap='gray')
    #plt.imshow
    cv2.waitKey(1)
    

    
   

    
