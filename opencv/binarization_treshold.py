import cv2
import os
import numpy as np


bot_resmi_yolu = os.path.join(os.getcwd(),"opencv","images","chp2","boat.jpg")
bot_resmi=cv2.imread(bot_resmi_yolu)
gri_bot = cv2.cvtColor(bot_resmi,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri bot",gri_bot)
# image = cv2.imread("opencv\\images\\chp2\\scanned_doc.png")
resim_yolu = os.path.join(os.getcwd(),"opencv","images","chp2","scanned_doc.png")
resim = cv2.imread(resim_yolu)
cv2.imshow("orijinal resim",resim)
#gri tonlamalı resim
gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
cv2.imshow("gri tonlamali",gri)
# print(resim.shape)
# print(gri.shape)
# eşikleme yolu ile resim siyah/beyaz dönüştürme
(T,sbResim1) = cv2.threshold(gri,60,255,cv2.THRESH_BINARY)
cv2.imshow("sb resim1",sbResim1)
# eşikleme yolu  ile resim siyah/beyaz olacak ama ters olarak
(Ti,sbResim2) = cv2.threshold(gri,60,255,cv2.THRESH_BINARY_INV)
cv2.imshow("sbResim2",sbResim2)
# uyarlanabilir(adaptive) threshold
sbResim3 = cv2.adaptiveThreshold(gri_bot,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,3)
cv2.imshow("uyarlanabilir",sbResim3)
print(T)
cv2.waitKey(0)