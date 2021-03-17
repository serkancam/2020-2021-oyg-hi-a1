import cv2
import os
kok_dizin = os.getcwd()
resim_yolu = os.path.join(kok_dizin,"opencv","images","chp1","marsrover.png")
resim = cv2.imread(resim_yolu)
# print(type(resim))

h,w,c = resim.shape
gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
cv2.imshow("mars rover",resim)
cv2.imshow("mars rover gri",gri)
print(resim.shape)
print(gri.shape)
# resim ilk piksel renk değeri
ilk_piksel=resim[0,0]
print("ilk piksel=",ilk_piksel)
# ilk 100 satır ve ilk 200 sutunu siyah yapalım
resim_degisik=resim.copy()
# resim_degisik[0:100,0:200]=(0,0,0)
resim_degisik[0:100,0:200]=resim_degisik[300:400,200:400]
cv2.rectangle(resim_degisik,(0,0),(200,100),(0,255,0),3)
# resim satır ve sutunların yarısını yok edelim
resim_kucuk = resim[::2,::2]
cv2.imwrite("degisik.jpg",resim_degisik)
cv2.imshow("değişik resim",resim_degisik)
cv2.imshow("kucuk resim",resim_kucuk)

# print(kok_dizin)
cv2.waitKey(0)