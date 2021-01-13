import cv2          #opencv
import os           #operating system / işletim sistemi
import numpy as np  #numpy

# path yol
cd = os.getcwd()# kaynak dizin current directory /   \

# print("kaynak dizin:",cd)
image_path = os.path.join(cd,"opencv","images","chp1","marsrover.png")
image = cv2.imread(image_path)
#resim boyut
print(type(image),image.shape,image.dtype)
#resim çözünürlüğü
shape = image.shape
h = shape[0]
w = shape[1]
print(f"resim {w}x{h}")
#ilk piksel rengi
ilk_px_rengi = image[0,0]
print(ilk_px_rengi)
image[0:100,0:200]=ilk_px_rengi#(0,255,0)

#resme çizgi çizelim
start = (100,70)
end =(350,380)
color = (0,255,255)
color2=(0,0,255)
thickness = 4
cv2.line(image,start,end,color,thickness)
# #dikdörtgen çizelim
cv2.rectangle(image,start,end,color2,thickness)

cv2.imshow("orijinal resim",image)

cv2.waitKey(0)