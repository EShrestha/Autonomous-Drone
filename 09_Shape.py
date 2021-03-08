import _DetectShape as ds
import cv2

cap = cv2.VideoCapture(0)
cap.set(400, 400)

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
        
        lstMax = max(counts)
        indexMax = counts.index(lstMax)
        confidence = (lstMax / count) * 100
        if indexMax == 1 and lstMax > 20: 
            print("Triangle" + f' Confidence: {confidence}%')
        elif indexMax == 2:
            print("Rectangle" + f' Confidence: {confidence}%')
            # drone do something for rectangle

        elif indexMax == 3:
            print("Circle" + f' Confidence: {confidence}%')
            #drone do something for circle
        else:
            print("Found nothing" + f' Confidence: {100 - confidence}%')
        count = 0
        counts = [-1, 0, 0, 0]

    key = cv2.waitKey(1)
    if key == 27:
        break
