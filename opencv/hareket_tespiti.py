import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
ret1,frame1=cap.read()
ret2,frame2=cap.read()
while cap.isOpened():
    #işlemler
    fark = cv2.absdiff(frame1,frame2)
    gri = cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    yumusak = cv2.GaussianBlur(gri,(5,5),0)
    t,sbResim = cv2.threshold(yumusak,20,255,cv2.THRESH_BINARY)
    yayilmis = cv2.dilate(sbResim,None,iterations=3)#görüntüdeki pikselleri yayar
    konturlar,_ = cv2.findContours(yayilmis,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for kontur in konturlar:
        (x,y,w,h) = cv2.boundingRect(kontur)
        print(cv2.contourArea(kontur))
        if cv2.contourArea(kontur)<2000:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"Hareket algilandi",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    # print(konturlar)
    #imshow
    cv2.imshow("resim1",frame1)
    # cv2.imshow("fark",fark)
    # cv2.imshow("gri/fark",gri)
    # cv2.imshow("gri/fark/blur",blur)
    # cv2.imshow("gri/fark/blur/iyah-beyaz",sbResim)
    # cv2.imshow("gri/fark/blur/iyah-beyaz/dilate",yayilmis)

    # frame değişimi
    frame1 = frame2   
    ret2,frame2=cap.read()
    if cv2.waitKey(40)==27:#27 escape tuşunun ascii de karakter kodu
        break

cv2.destroyAllWindows()
cam.release()