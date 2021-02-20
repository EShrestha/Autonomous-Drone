import _DetectShape as ds
import cv2

cap = cv2.VideoCapture(0)
cap.set(200, 200)

count = 0
counts = [-1,0,0,0]

while True:
    _, frame = cap.read()

    #cv2.imshow("Capture Shape",frame)
    #print(ds.getShape(frame))
    num = ds.getShape(frame)
    if num == 1: counts[1] += 1
    if num == 2: counts[2] += 1
    if num == 3: counts[3] += 1
    count += 1
    if count > 100:
        count = 0
        lstMax = max(counts)
        indexMax = counts.index(lstMax)
        if indexMax == 1: 
            print("Triangle")
            

        if indexMax == 2:
            print("Rectangle")
            # drone do something for rectangle

        if indexMax == 3:
            print("Circle")
            #drone do something for circle
        else:
            print("Found nothing")
        counts = [-1, 0, 0, 0]

    key = cv2.waitKey(1)
    if key == 27:
        break
