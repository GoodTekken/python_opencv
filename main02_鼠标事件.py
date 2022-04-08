#查看所有被支持的鼠标事件
# https://www.kancloud.cn/aollo/aolloopencv/261446

import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

#mouse callback function

def draw_circle(event,x,y,flags,param):
    if(event == cv2.EVENT_LBUTTONDBLCLK):  #双击鼠标左键
        cv2.circle(img,(x,y),100,(255,0,0),-1)



def draw_circle2(event,x,y,flags,param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y

    elif event == cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode ==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),3,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing ==False

#创建图像与窗口并将窗口与回调函数绑定
img = np.zeros((500,500,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle2)
mode = False

while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'): #按q键退出
        break

cv2.destroyAllWIndows()