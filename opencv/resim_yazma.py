import cv2
import os
import numpy as np
canvas_r = np.zeros((200,200,3),dtype=np.uint8) 
canvas_c = canvas_r.copy()#np.zeros((200,200),dtype=np.uint8) 
# dikdörtgen çizelim
start =(10,10)
end=(100,100)
color = (150,150,0)
center =(100,100)
radius = 50
t = 5
cv2.rectangle(canvas_r,start,end,color,t)
cv2.circle(canvas_c,center,radius,color,-1)

cv2.imshow("rectangle",canvas_r)
cv2.imshow("circle",canvas_c)

cd = os.getcwd()
c_path=os.path.join(cd,"opencv","images","chp1","circle.jpg")
r_path=os.path.join(cd,"opencv","images","chp1","rectangle.jpg")
cv2.imwrite(r_path,canvas_r)
cv2.imwrite(c_path,canvas_c)
cv2.waitKey(0)