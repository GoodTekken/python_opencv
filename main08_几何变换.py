import cv2
# https://www.kancloud.cn/aollo/aolloopencv/264331
img = cv2.imread('./Image/Luffy.jpg')

# 扩展缩放 在缩放时推荐cv2.INTER_AREA，在拓展时推荐cv2.INTER_CUBIC（慢）和cv2.INTER_LINEAR
# 默认情况下所有改变图像尺寸大小的操作使用的是插值法都是cv2.INTER_LINEAR
#下面的None本应该是输出图像的尺寸，但是因为后面我们设置了缩放因子，所以，这里为None
res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

height , width =img.shape[:2]
res1 = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

# cv2.imshow('img',img)
# cv2.imshow('res',res)
# cv2.imshow('res1',res1)

# 平移
# img.shape[:2] 取彩色图片的长、宽。
# 如果img.shape[:3] 则取彩色图片的长、宽、通道
# img.shape[0]：图像的垂直尺寸（高度）
# img.shape[1]：图像的水平尺寸（宽度）
# img.shape[2]：图像的通道数
# rows = img.shape[0]
# cols = img.shape[1]
rows,cols = img.shape[:2]

#这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
#可以通过设置旋转中心，缩放因子以及窗口大小来防止旋转后超出边界的问题。
M=cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)
#第三个参数是输出图像的尺寸中心
dst=cv2.warpAffine(img,M,(2*cols,2*rows))

cv2.imshow('img',img)

cv2.imshow('M',M)

cv2.imshow('dst',dst)


cv2.waitKey(0)



# 旋转


cv2.waitKey(0)