from djitellopy import tello
import _KeyPress as kp
import numpy as np
import cv2
import math
from time import sleep


########## PARAMETERS ############

fspeed = 117/10 # Forward speed cm/s (15cm/1s)
aspeed = 360/10 # Angular Speed degrees/s (50d/1s)
interval = .25


dInterval = fspeed*interval
aInterval = aspeed*interval

##################################

x, y = 500, 500
angle = 0
yaw = 0



kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

points = [(0,0), (0,0)]

def getKeyboardInput():
    # Setting left/right, forward/backward, up/down, and yaw velocity to 0
    lr, fb, ud, yv = 0, 0, 0, 0
    SPEED = 15  # Number of cm the drone moves on a key press
    angularSpeed = 50
    global x, y, angle, yaw
    distance = 0

    if kp.getKey("LEFT"):
        lr = -SPEED       # -X direction
        distance = dInterval
        angle = -180

    elif kp.getKey("RIGHT"):
        lr = SPEED       # +X direction
        distance = -dInterval
        angle = 180

    if kp.getKey("UP"):
        fb = SPEED          # +Z direction
        distance = dInterval
        angle = 270

    elif kp.getKey("DOWN"):
        fb = -SPEED       # -Z direction
        distance = -dInterval
        angle = -90

    if kp.getKey("w"):
        ud = SPEED           # +Y direction

    elif kp.getKey("s"):
        ud = -SPEED          # -Y direction


    if kp.getKey("a"):
        yv = -angularSpeed           # -X rotation
        yaw -= aInterval

    elif kp.getKey("d"):
        yv = angularSpeed            # +X rotation
        yaw += aInterval

    if kp.getKey("e"): drone.takeoff()      # Drone takes off
    if kp.getKey("q"): drone.land()         # Drone Lands

    sleep(interval)
    angle += yaw
    x += int(distance*math.cos(math.radians(angle)))
    y += int(distance*math.sin(math.radians(angle)))
    

    return [lr, fb, ud, yv, x, y]


def drawPoints(img, points):
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)

    cv2.circle(img, points[-1], 8, (0, 215, 255), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0]-500)/100},{(points[-1][1]-500)/100})m', (points[-1][0]+10, points[-1][1]+30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 215, 255), 2)


while True:
    values = getKeyboardInput()
    drone.send_rc_control(values[0], values[1], values[2], values[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    if(points[-1][0] != values[4] or points[-1][1] != values[5]):
        points.append((values[4], values[5]))
    drawPoints(img, points)
    cv2.imshow("Mapping", img)
    cv2.waitKey(1)
