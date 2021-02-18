from djitellopy import tello
import _KeyPress as kp
from time import sleep

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())


while True:
    print(drone.get_height) #getting weird stuff in the console
    #test methods
    print(drone.get_distance_tof)
    #lots of scanning images since there doesn't seem to be a sensor on the drone to detect around it
    # Load an color image in grayscale
    img = cv2.imread('messi5.jpg',0)
    #CV2 will probably be important
