#===================================================================Import==========================================================
import cv2
import time
import numpy as np
import HandTrackModule as htm
import math
from cvzone.SerialModule import SerialObject
from time import sleep

#####################################################
wCam, hCam = 640, 480
#####################################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime=0
arduino = SerialObject()

detector = htm.handDetector(detectionCon=0.7, maxHands=1)





brightBar = 400
brightPer = 0
brightLed = 0
area = 0
#===================================================================Functionality=====================================================
try:
    while True:
        success, img = cap.read()

        # Find Hand
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img, draw=True)
        if len(lmList) !=0:

            # Filter based on size
            area = (bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
            if 250<area<1000:

                # Find Distance between index and thumb

                length, img, lineInfo = detector.findDistance(4,8,img)

                # Convert brightness
                brightBar = np.interp(length, [50, 200], [400, 150])
                brightPer = np.interp(length, [50, 200], [0, 100])
                brightLed = np.interp(length, [50, 200], [0, 255])

                # Reduce Resolution to it smoother
                smoothness = 5
                brightPer = smoothness * round(brightPer/smoothness)

                # Check fingers up
                fingers = detector.fingersUp()

                # if pinky down set brightness
                if not fingers[4]:
                    arduino.sendData([brightLed])
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 8, (0, 255, 0), cv2.FILLED)





                if length<50:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 8, (0,136,8), cv2.FILLED)

        # Drawings
        cv2.rectangle(img, (50,150),(85,400), (255,0,0), 2)
        cv2.rectangle(img, (50, int(brightBar)), (85, 400), (255,0,0), cv2.FILLED)
        cv2.putText(img, f': {int(brightPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255,0,0), 2)
        cBright = int(brightLed*100)


        # Frame rate
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255,0,0), 2)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
#=================================================================Ignore Exceptions 🙂=======================================================

except Exception:
    pass
except KeyboardInterrupt:
    pass
