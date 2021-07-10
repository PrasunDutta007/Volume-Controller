import cv2
import mediapipe as mp
import time
import numpy as np
import imutils

url = "https://192.168.2.8:8080/video"
cap = cv2.VideoCapture(0)

#initializing hand module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

#Hand-info
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                #if id == 4:
                cv2.circle(img, (cx,cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
#FPS
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

#FPS-dsiplay
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

