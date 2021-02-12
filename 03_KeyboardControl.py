from djitellopy import tello
import _KeyPress as kp
from time import sleep

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())



def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0 # Setting left/right, forward/backward, up/down, and yaw velocity to 0
    SPEED = 50 # Number of cm the drone moves on a key press
    TURN = 50

    if kp.getKey("LEFT"): lr = -SPEED       # -X direction
    if kp.getKey("RIGHT"): lr = SPEED       # +X direction

    if kp.getKey("UP"): fb = SPEED          # +Z direction
    if kp.getKey("DOWN"): fb = -SPEED       # -Z direction

    if kp.getKey("w"): ud = SPEED           # +Y direction
    if kp.getKey("s"): ud = -SPEED          # -Y direction

    if kp.getKey("a"): yv = -TURN           # -X rotation
    if kp.getKey("d"): yv = TURN            # +X rotation


    if kp.getKey("e"): drone.takeoff()      # Drone takes off
    if kp.getKey("q"): drone.land()         # Drone Lands

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
