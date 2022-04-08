# 基本操作为腐蚀和膨胀，他们的变体构成了开运算，闭运算，梯度等。
# https://www.kancloud.cn/aollo/aolloopencv/270208

import cv2
import numpy as np

img = cv2.imread('./Image/Luffy.jpg',1)
kernel = np.ones((5,5),np.uint8)
#1，腐蚀
erosion = cv2.erode(img,kernel,iterations=1)
#2，膨胀
dilate = cv2.dilate(img,kernel,iterations=1)
#3，开运算
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
#4，闭运算
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
#5，形态学梯度
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

# 6.礼帽
# 原始图像与进行开运算之后得到的图像的差。
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

# 7.黑帽
# 进行闭运算之后得到的图像与原始图像的差。
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

while(1):
    cv2.imshow('image',img)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation', dilate)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    cv2.imshow('gradient', gradient)
    cv2.imshow('tophat', tophat)
    cv2.imshow('blackhat', blackhat)

    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()


