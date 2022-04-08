import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./Image/Luffy.jpg')

# blur = cv2.blur(img,(5,5))   #平均
# blur = cv2.GaussianBlur(img,(5,5),0) #高斯模糊
# blur = cv2.medianBlur(img,5)   #中指迷糊

#cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
#d – Diameter of each pixel neighborhood that is used during filtering. # If it is non-positive, it is computed from sigmaSpace
# 9 邻域直径，两个 75 分别是空间高斯函数标准差，灰度值相似性高斯函数标准差
blur = cv2.bilateralFilter(img,9,75,75)  #双边滤波

while(1):
    cv2.imshow('image',img)
    cv2.imshow('blur',blur)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()