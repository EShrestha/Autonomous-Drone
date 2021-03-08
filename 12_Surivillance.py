from djitellopy import tello
from time import sleep
import numpy as np
import cv2
import time
from random import randrange
import datetime

drone = tello.Tello()
drone.connect()
print(drone.get_battery())
#cap = cv2.VideoCapture(0)

drone.streamon()
drone.takeoff()

for_back_velocity = 0
rotate_velocity = 0
while True:
    frame = drone.get_frame_read().frame
    frame = cv2.resize(frame, (360, 240))
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    noWhite = cv2.bitwise_and(frame, frame, mask=mask)

    noWallPercent = ((np.sum(mask) / np.size(mask)/255) * 100)
    wallPercent = 100 - noWallPercent
    print(f'NO Wall: {noWallPercent}  | Wall Percent: {wallPercent}')

    cv2.putText(frame, f"Wall?: {wallPercent}", (0, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

    if(wallPercent < 60):
        cv2.putText(frame, "Move: Forward", (0, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        for_back_velocity = 20
        rotate_velocity = 0
        rand = randrange(100)+1
        if(rand < 6):
            now = datetime.datetime.now()
            cv2.putText(frame, "Capturing Image", (0, 60),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, "Time: " +f'{now.hour}:{now.minute}', (0, 80),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

            cv2.imwrite(f'Surveillance/Images/{time.time()}.jpg', frame) # Captures and writes image to the folder
            time.sleep(0.3) # Short delay after captureing image

    elif (wallPercent > 90):
        cv2.putText(frame, "Move: Backwards", (0, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        for_back_velocity = -20
        rotate_velocity = 20

    else:
        cv2.putText(frame, "Move: Rotate", (0, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        rotate_velocity = 32
        for_back_velocity = 0

    drone.send_rc_control(0, for_back_velocity, 0, rotate_velocity)

    cv2.imshow("Drone Image", frame)
    cv2.imshow("Mask", mask)
    cv2.waitKey(1)
