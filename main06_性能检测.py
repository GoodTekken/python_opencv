import cv2
import numpy as np


# https://www.kancloud.cn/aollo/aolloopencv/263721
img1 = cv2.imread('./Image/wei.jpg')

e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
time = (e2-e1)/cv2.getTickFrequency()
print(time)

cv2.imshow('img1',img1)


cv2.waitKey(0)