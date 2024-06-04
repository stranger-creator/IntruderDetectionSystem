import cv2
import send
cap=cv2.VideoCapture(0)
from cvzone.PoseModule import PoseDetector
detector = PoseDetector()
cap.set(3,640)
cap.set(4,480)
l=[]
flag=True
while True:
    success,img = cap.read()
    img = detector.findPose(img)
    imlist,bbox = detector.findPosition(img)
    if len(imlist) > 0:
        print("Human face is detected")
        print(imlist)
        l.append(1)
    if len(l)>50 and flag:
        flag=False
        send.SendSms()
    cv2.imshow("output",img)
    q=cv2.waitKey(1)
    if q==ord('q'):
        break