import numpy as np
import cv2

img = cv2.imread('./Image/wei.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy=cv2.findContours(thresh,1,2)
cnt=contours[0]
print(cnt)
M=cv2.moments(cnt)
print(M)

# 轮廓面积
area=cv2.contourArea(cnt)
print(area)

# 轮廓周长
perimeter = cv2.arcLength(cnt,True)
print(perimeter)

x,y,w,h=cv2.boundingRect(cnt)
img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('img', img)

# 直线拟合
rows,cols = img.shape[:2]
[vx,vy,x,y]=cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
lefty=int((x*vy/vx)+y)
righty=int(((cols-x)*vy/vx)+y)
img2 = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
cv2.imshow('img2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

