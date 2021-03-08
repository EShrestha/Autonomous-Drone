from djitellopy import tello
import cv2
import numpy as np


def initializeTello():
    myDrone = tello.Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0
    myDrone. left_right_velocity = 0
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity = 0
    myDrone.speed = 0
    print(myDrone.get_battery())
    myDrone.streamoff()
    myDrone.streamon()
    return myDrone


def telloGetFrame(myDrone, w=360, h=240):
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame, (w, h))
    return img


def findFace(img, myDrone):
    faceCascade = cv2.CascadeClassifier(
        'Resources/haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 6)

    myFaceListC = []
    myFaceListArea = []

    width = 0

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        width = w
        cx = x + w//2
        cy = y + h//2
        area = w*h
        myFaceListArea.append(area)
        myFaceListC.append([cx, cy])

    followFace(width, myDrone, img)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]


def followFace(w, myDrone, img):
    print("WIDTH: ", w)
    #60ish is an optimal width
    #the lowest size it was detecting was at 25 (any more and no detection)
    if(w < 40 and w > 0):
        cv2.putText(img, "Move: Forward", (0, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        myDrone.send_rc_control(0, 15, 2, 0)
    elif (w > 60):
        cv2.putText(img, "Move: Back", (0, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        myDrone.send_rc_control(0, -15, 2, 0)
    elif (w >= 40 and w <= 60):
        cv2.putText(img, "Move: TARGET!", (0, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        myDrone.send_rc_control(0, 100, 2, 0)
    else:
        cv2.putText(img, "Move: Steady", (0, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)


def trackFace(myDrone, info, w, pid, pError):

    ## PID
    error = info[0][0] - w//2
    speed = pid[0]*error + pid[1]*(error-pError)
    speed = int(np.clip(speed, -100, 100))

    #print(speed)
    if info[0][0] != 0:
        #print("ERROR amount: ", info[0][0])
        myDrone.yaw_velocity = speed  # left right turn speed

    else:  # Else stand still
        myDrone.for_back_velocity = 0
        myDrone.left_right_velocity = 0
        myDrone.up_down_velocity = 0
        myDrone.yaw_velocity = 0
        #myDrone.send_rc_control(0, 100, 0, 0) # Crash into face
        error = 0
    if myDrone.send_rc_control:
        myDrone.send_rc_control(myDrone.left_right_velocity, myDrone.for_back_velocity,
                                myDrone.up_down_velocity, myDrone.yaw_velocity)
    return error
