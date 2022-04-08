import cv2
import numpy

# https://www.kancloud.cn/aollo/aolloopencv/262768
#获取并修改像素值
img = cv2.imread('./Image/Luffy.jpg')
px = img[100,100]
print(px)

blue = img[100,100,2]  #参数3：获取其中通道的值
print(blue)

img[101,101] = [255,255,255]
print(img[101,101])

print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))

#获取图像属性
print(img.shape)  #包含行数，列数和通道数

#获取图像的像素数目
print(img.size)

#图像ROI 对图像的特定区域操作
ball = img[0:100,200:0]
img[100:200,300:100]=ball



#拆分及合并图像通道
r,g,b = cv2.split(img)  #拆分
# img=cv2.merge(r,g,b)  #把独立通道的图片合成一个RGB

b = img[:,:,0] #拆分b通道

#红色通道值设为0
img[:,:,2]=0

#cv2.split()是比较耗时的操作，能使用numpy就尽量使用


cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)
# cv2.imwrite('./Image/myluffy.png', img)


#加入边框颜色
from matplotlib import pyplot as plt
blue = [255,0,0]
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=blue)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')

plt.show()


k = cv2.waitKey(0)
