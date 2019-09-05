import numpy as np
import cv2
from pathlib import Path
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-vn1", "--video1", required=True,
                help="Path to video file to be placed on right")
ap.add_argument("-vn2", "--video2", required=True,
                help="Path to video file to be placed on left")
ap.add_argument("-a", "--axis", type=int, default=1,
                help="Mention along which axis you want to concatenate the video: along x = 1 along y = 0")
args = vars(ap.parse_args())

cap1 = cv2.VideoCapture(args["video1"])
cap2 = cv2.VideoCapture(args["video2"])
path = args["video1"]
name1 = Path(path).stem
path = args["video2"]
name2 = Path(path).stem
print ("[Info]: Video file loaded")
fps = cap1.get(cv2.CAP_PROP_FPS)
widthcap1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
heightcap1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
widthcap2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
heightcap2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
if args["axis"] is 1:
    out = cv2.VideoWriter(name1+'-'+name2+'.mp4', fourcc, fps, ((widthcap1+widthcap2), heightcap1))
else:
    out = cv2.VideoWriter(name1+'-'+name2+'.mp4', fourcc, fps, (widthcap1, (heightcap1+heightcap2)))
while(cap1.isOpened()):
    ret, frame = cap1.read()
    ret1, frame1 = cap2.read()

    if frame1 is None:
        break

    ff = np.concatenate((frame, frame1), axis=args["axis"])
    if args["axis"] is 1:
        resized = cv2.resize(ff, ((widthcap1+widthcap2), heightcap1),
                         interpolation=cv2.INTER_CUBIC)
    else:
        resized = cv2.resize(ff, (widthcap1, (heightcap1+heightcap2)),
                             interpolation=cv2.INTER_CUBIC)

    out.write(resized)

    # cv2.imshow('frame', ff)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
print("[Info]: Video file saved")
cap1.release()
cap2.release()
cv2.destroyAllWindows()
