import cv2
import numpy as np
import random
import os

# print(random.randint(1,30))
# print(random.uniform(1.0,2.0))
cd = os.getcwd()
image = np.zeros((400, 800, 3), dtype=np.uint8)
image_path1 = os.path.join(cd, "opencv", "images", "chp2", "zebra.png")
image_path2 = os.path.join(cd, "opencv", "images",
                           "chp2", "soccer-in-green.jpg")
image1 = cv2.imread(image_path1)
image2 = cv2.imread(image_path2)

image1 = cv2.resize(src=image1, dsize=(400, 400), interpolation=cv2.INTER_AREA)
image2 = cv2.resize(src=image2, dsize=(400, 400), interpolation=cv2.INTER_AREA)
image[::,0:400]=image1
image[::,400:]=image2


cv2.imshow("toplama", image)

cv2.waitKey(0)
