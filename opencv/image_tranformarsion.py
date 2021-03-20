import cv2
import numpy as np
import os

cd = os.getcwd()
image_path = os.path.join(cd,"opencv","images","chp2","zebrasmall.png")
image_original =cv2.imread(image_path)
# değerler
h,w,c = image_original.shape
merkez = (w//2,h//2)
aci = 30
boyut = 1.0
# rotasyon matrisi
r_m1 = cv2.getRotationMatrix2D(merkez,aci,boyut)
r_m2 = cv2.getRotationMatrix2D((0,0),-30,0.5)
# bu matris ile yeni image oluştur
image_r1 = cv2.warpAffine(image_original,r_m1,(w,h))
image_r2 = cv2.warpAffine(image_original,r_m2,(w,h))

# resmi ana görüntüsü
image_fh = cv2.flip(image_original,1)#1 yatay 0 dikey -1 hem yatay hem dikey çevirme
image_fv = cv2.flip(image_original,0)#1 yatay 0 dikey -1 hem yatay hem dikey çevirme

cv2.imshow("orijinal",image_original)
cv2.imshow("donen 1",image_r1)
cv2.imshow("donen 2",image_r2)
cv2.imshow("yatay çevirme",image_fh)
cv2.imshow("dikey çevirme",image_fv)
cv2.waitKey(0)