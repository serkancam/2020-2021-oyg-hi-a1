import cv2,os
import  numpy as np

cd =  os.getcwd()
resim_yolu = os.path.join(cd,"numpy","bo2.png")


image = cv2.imread(resim_yolu)
print(image.shape)
image_cut = image[0:250,600:803,0:3]
# cv2.imshow("ana_resim",image)
cv2.imshow("kesik_resim",image_cut)
cv2.waitKey(0)
# img = Image.fromarray(image,"RGB")
# img.show()
