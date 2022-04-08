# https://docs.oakchina.cn/en/latest/pages/preface.html
# https://www.kancloud.cn/aollo/aolloopencv/263731


import cv2
import numpy as np

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

# 在 OpenCV 的 HSV 格式中，H（色彩/色度）的取值范围是 [0，179]， S（饱和度）的取值范围 [0，255]，V（亮度）的取值范围 [0，255]。但是不同的软件使用的值可能不同。
# 一定要记得归一化处理。

img = cv2.imread('./Image/wei.jpg')

# 转换到HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# 设定蓝色的阈值
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# 根据阈值构建掩膜
mask = cv2.inRange(hsv,lower_blue,upper_blue)
# 对原图和掩膜进行位运算
res = cv2.bitwise_and(img,img,mask=mask)
# 显示图像
cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

green=np.uint8([[[0,255,0]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print (hsv_green )

cv2.waitKey(0);