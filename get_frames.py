import os
import cv2
import pandas as pd
import re
from tqdm import tqdm
ann = pd.read_csv('./annotations.csv', delimiter ='\t')

ann = ann[ann['train'] == True]

def remove_special_characters(string):
  pattern = r'[^\d\w\sА-Яа-я]'
  string = re.sub(pattern, '', string)
  return string

video_dir_path = "/path/to/video"
path_of_labels = "/path/labels"

for i, row in tqdm(ann.iterrows(), total=ann.shape[0]):
  text = row['text']
  attachment_id = row['attachment_id']
  
  video_path = os.path.join(video_dir_path, attachment_id + '.mp4')
  path_of_label = os.path.join(path_of_labels, remove_special_characters(text))

  if not os.path.exists(path_of_label):
    os.mkdir(path_of_label)
  if len(os.listdir(path_of_label)) < 3:
    image_path = os.path.join(path_of_label, attachment_id)
    if not os.path.exists(image_path):
      os.mkdir(image_path)
    cap = cv2.VideoCapture(video_path)
    k = 0
    while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
          break
      if k % 6 == 0:
        save = os.path.join(image_path, f'{k}.jpg')
        save = save.replace('\\', '/')
        cv2.imencode(".jpg",frame)[1].tofile(save)
      k += 1
    cap.release()