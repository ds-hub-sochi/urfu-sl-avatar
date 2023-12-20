from cvzone.HandTrackingModule import HandDetector
import pandas as pd
import cv2
import os

path_to_train = './rain/'
names_video = os.listdir(path_to_train)
detector = HandDetector(detectionCon=0.8, maxHands=2)

df = pd.read_csv('df_embed.csv')
counter = 0
for name_video in names_video:
    
    full_data = []
    full_path = path_to_train + name_video
    cap = cv2.VideoCapture(full_path)
    success, img = cap.read()
    while cap.isOpened():
    # Get image frame
        success, img = cap.read()
        if not success:
            data = []
            break

        # Find the hand and its landmarks
        hands, img = detector.findHands(img)
        # One hand:
        if len(hands) == 1:
            hand = hands[0]
            handType = hand["type"]
            data = [1, handType]
            lmList = hand["lmList"]  # List of 21 Landmark points
            for lm in lmList:
                data.extend([lm[0], lm[1], lm[2]])
            full_data.append(data)
        
        # Two hands:
        if len(hands) == 2:
            data = [2]
            for hand in hands:
                handType = hand["type"]
                data.append(handType)
                lmList = hand["lmList"]  # List of 21 Landmark points
                for lm in lmList:
                    data.extend([lm[0], lm[1], lm[2]])
            full_data.append(data)
    if len(full_data) != 0:

        if full_data[0][0] == 1:
            df.loc[df['attachment_id'] == name_video[:-4], f"{full_data[0][1]}_start"] = str(full_data[0][2:])


        elif full_data[-1][0] == 1:
            df.loc[df['attachment_id'] == name_video[:-4], f"{full_data[-1][1]}_end"] = str(full_data[-1][2:])

        if full_data[0][0] == 2:
            df.loc[df['attachment_id'] == name_video[:-4], f"{full_data[0][1]}_start"] = str(full_data[0][2:65])
            df.loc[df['attachment_id'] == name_video[:-4], f"{full_data[0][65]}_start"] = str(full_data[0][66:])

        elif full_data[-1][0] == 2:
            df.loc[df['attachment_id'] == name_video[:-4], f"{full_data[-1][1]}_end"] = str(full_data[-1][2:65])
            df.loc[df['attachment_id'] == name_video[:-4], f"{full_data[-1][65]}_end"] = str(full_data[-1][66:])
        counter+=1
        print(f'Обработано {counter}/{len(names_video)}')
    else:
        print('Не найдены точки')
        pass
df.to_csv('./f_points.csv')