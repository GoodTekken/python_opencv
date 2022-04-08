# https://www.kancloud.cn/aollo/aolloopencv/267591

# 1，简单阈值
#  cv2.threshold cv2.adaptiveThreshold

# 当像素值高于阀值时，我们给这个像素赋予一个新值（可能是白色），否则我们给它赋予另外一种颜色（也许是黑色）

import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt2

img = cv2.imread('./Image/Luffy.jpg')
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['original image','Binary','binary-inv','trunc','tozero','tozero-inv']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i][:, :, ::-1],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
plt2.subplot(2,2,1)
# plt2.imshow(img, cmap='gray')
# plt2.imshow(img, cmap='None')
plt2.title('pic 1')
plt2.xticks([])
plt2.yticks([])
# plt2.show()
plt2.imshow(img[:, :, ::-1],'gray')
plt2.show()

cv2.imshow('img',img)
cv2.imshow('thresh5',thresh5)
cv2.waitKey(0)