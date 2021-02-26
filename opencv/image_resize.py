import cv2
import numpy as np
import random
import os

# print(random.randint(1,30))
# print(random.uniform(1.0,2.0))
cd = os.getcwd()
# 1. yöntem
image_path = os.path.join(cd,"opencv","images","chp2","zebra.png")
# print(image_path)
image_o = cv2.imread(image_path)
#
h,w,c = image_o.shape
aspect_ratio=w/h#0.5 uydurma
h_new =int(h*0.2)#335.5
w_new =int(h_new*aspect_ratio)#175.2-->175

image_r1 = cv2.resize(src=image_o,dsize=(h_new,w_new),interpolation=cv2.INTER_AREA)
# 2. yöntem
image_path2 = os.path.join(cd,"opencv","images","chp2","soccer-in-green.jpg")
image2=cv2.imread(image_path2)

image2_big=cv2.resize(src=image2,dsize=None,fx=2.0,fy=2.0,interpolation=cv2.INTER_LINEAR)

cv2.imshow("soccer original",image2)
cv2.imshow("soccer big",image2_big)

cv2.imshow("original",image_o)
cv2.imshow("r1",image_r1)
cv2.waitKey(0)

# INTER_LINEAR: Bu aslında en yakın dört komşunun (2 × 2 = 4) belirlendiği ve bir sonraki pikselin değerini belirlemek için ağırlıklı ortalamasının hesaplandığı bir çift doğrusal enterpolasyondur. 

# INTER_NEAREST: Bu, o noktanın etrafındaki noktalarda (komşu) noktalarda o fonksiyonun değeri verildiğinde, bir boşluktaki bir olmayan nokta için bir fonksiyonun değerini tahmin etmek için en yakın komşu enterpolasyon yöntemini kullanır. Başka bir deyişle, bir pikselin değerini hesaplamak için, en yakın komşusunun enterpolasyon fonksiyonuna yaklaştığı kabul edilir. 

# INTER_CUBIC: Bu, piksel değerini hesaplamak için bikübik enterpolasyon algoritması kullanır. Çift doğrusal enterpolasyona benzer şekilde, bir sonraki pikselin değerini belirlemek için 4 × 4 = 16 en yakın komşuyu kullanır. Hız bir sorun olmadığında, bikübik enterpolasyon, çift doğrusal ile karşılaştırıldığında daha iyi yeniden boyutlandırılmış bir görüntü sağlar. 

# INTER_LANCZOS4: Bu, 8 × 8 en yakın komşu enterpolasyonunu kullanır. 

# INTER_AREA: Piksel değerinin hesaplanması, piksel alanı ilişkisi kullanılarak gerçekleştirilir (OpenCV resmi belgelerinde açıklandığı gibi). Bu algoritmayı hareli olmayan yeniden boyutlandırılmış bir görüntü oluşturmak için kullanıyoruz. Görüntü boyutu büyütüldüğünde, INTER_AREA INTER_NEAREST yöntemine benzer.