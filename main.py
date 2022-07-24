import cv2
import mediapipe as mp
capturing_image = cv2.VideoCapture(0)
Hands = mp.solutions.hands
hands = Hands.Hands()
Draw = mp.solutions.drawing_utils
while True:
    success, img = capturing_image.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            Draw.draw_landmarks(img, handLms, Hands.HAND_CONNECTIONS)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
