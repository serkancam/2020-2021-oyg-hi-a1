import cv2
import os
import numpy as np

bulundugumuz_dizin = os.getcwd()
# print(30*"*",bulundugumuz_dizin,30*"*")
resim_yolu = os.path.join(bulundugumuz_dizin,"opencv","images","chp2","n4.jpg")
# print(30*"*",resim_yolu,30*"*")
resim = cv2.imread(resim_yolu)
cv2.imshow("orijinal resim",resim)

yumusatilmis_3 = cv2.medianBlur(resim,3)
cv2.imshow("yumusatilmis 3",yumusatilmis_3)

yumusatilmis_5 = cv2.medianBlur(resim,5)
cv2.imshow("yumusatilmis_5",yumusatilmis_5)

cv2.waitKey(0)
