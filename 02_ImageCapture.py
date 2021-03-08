from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())


drone.streamon()

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(720,480))
    cv2.imshow("Drone ", img)
    cv2.waitKey(1)