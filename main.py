from cvzone.HandTrackingModule import HandDetector
import cv2
import socket


video_path = 'Path/to/video'
cap = cv2.VideoCapture(video_path)
success, img = cap.read()
h, w, _ = img.shape

detector = HandDetector(detectionCon=0.8, maxHands=2)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

while cap.isOpened():
    # Get image frame
    success, img = cap.read()
    if not success:
        data = []
        break

    # Find the hand and its landmarks
    hands, img = detector.findHands(img)

    # One hand
    if len(hands) == 1:
        hand = hands[0]
        handType = hand["type"]
        if handType == "Right":
            handType = 1
        else:
            handType = 2
        data = [1, handType]
        lmList = hand["lmList"]  # List of 21 Landmark points
        for lm in lmList:
            data.extend([lm[0], h - lm[1], lm[2]])
        # print(data) # list with 65 values
        sock.sendto(str.encode(str(data)), serverAddressPort)
    
    # Two hands
    if len(hands) == 2:
        data = [2, "Both"]
        for hand in hands:
            lmList = hand["lmList"]  # List of 21 Landmark points
            for lm in lmList:
                data.extend([lm[0], h - lm[1], lm[2]])
        # print(data) # list with 128 values
        sock.sendto(str.encode(str(data)), serverAddressPort)

    # Display
    # cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
    # cv2.imshow('custom window', img)
    # cv2.resizeWindow('custom window', 640, 1280)
    # cv2.waitKey(1)

cap.release()
# cv2.destroyAllWindows()

