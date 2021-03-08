from djitellopy import tello
import _KeyPress as kp
import time
import cv2

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

global img

drone.streamon()


def getKeyboardInput():
    # Setting left/right, forward/backward, up/down, and yaw velocity to 0
    lr, fb, ud, yv = 0, 0, 0, 0
    global keypress
    keypress = "-"
    SPEED = 50  # Number of cm the drone moves on a key press
    TURN = 75   # Different number for faster turning speed

    if kp.getKey("LEFT"):
        keypress = "<"
        lr = -SPEED         # -X direction
    if kp.getKey("RIGHT"):
        keypress = ">"
        lr = SPEED          # +X direction

    if kp.getKey("UP"):
        keypress = "^"
        fb = SPEED          # +Z direction
    if kp.getKey("DOWN"):
        keypress = "V"
        fb = -SPEED         # -Z direction

    if kp.getKey("w"):
        keypress = "w"
        ud = SPEED           # +Y direction
    if kp.getKey("s"):
        keypress = "s"
        ud = -SPEED          # -Y direction

    if kp.getKey("a"):
        keypress = "a"
        yv = -TURN           # -X rotation
    if kp.getKey("d"):
        keypress = "d"
        yv = TURN            # +X rotation

    if kp.getKey("e"):
        drone.takeoff()      # Drone takes off
    if kp.getKey("q"):      # Drone Lands
        keypress = "q"
        drone.land()
        time.sleep(3)         

    if kp.getKey("z"):
        cv2.imwrite(f'Surveillance/Images/{time.time()}.jpg', img) # Captures and writes image to the folder
        time.sleep(0.3) # Short delay after captureing image

    return [lr, fb, ud, yv]


while True:
    values = getKeyboardInput()
    drone.send_rc_control(values[0], values[1], values[2], values[3])
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (720, 480))
    cv2.putText(img, f'Key Pressed: {keypress}', (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imshow("Drone Image", img)
    cv2.waitKey(1)
