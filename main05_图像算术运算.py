# https://www.kancloud.cn/aollo/aolloopencv/263215

import cv2
import numpy as np


# 1，图像加法
x=np.uint8([250])
y=np.uint8([10])
print(cv2.add(x,y))  #250+10=260>=255
#结果为255    openCV的加法是一种饱和操作，

print(x+y) #250+10=260%255=4
# 结果为4  而numpy的加法是一种模操作

# 2，图像混合

img1=cv2.imread('./Image/Luffy.jpg') #224*346
img2=cv2.imread('./Image/wei.jpg')

img = np.zeros((346,224,3),np.uint8)

e1 = cv2.getTickCount()

for i in range(346):
    for j in range(224):
        img[i, j, 0] = img2[i, j, 0]
        img[i, j, 1] = img2[i, j, 1]
        img[i, j, 2] = img2[i, j, 2]

e2 = cv2.getTickCount()
time = (e2-e1)/cv2.getTickFrequency()
print(time)


print(img1.shape)  #包含行数，列数和通道数
print(img.shape)  #包含行数，列数和通道数



print(img1.size)
print(img.size)


dst = cv2.addWeighted(img1,0.3,img,0.7,0)
cv2.imshow('dst',dst)

#I want to put logo on top left corner,SO I create a ROI
rows,cols,channels = img1.shape
roi = img2[0:rows,0:cols]

img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,175,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img2_bg=cv2.bitwise_and(roi,roi,mask=mask)
cv2.imshow('img2_bg',img2_bg)

img1_fg = cv2.bitwise_and(img1,img1,mask=mask_inv)
cv2.imshow('img1_fg',img1_fg)

dst = cv2.add(img2_bg,img1_fg)
img2[0:rows,0:cols]=dst

cv2.imshow('res',img2)


cv2.waitKey(0)
cv2.destroyWindow()