# 就是同一图像的不同分辨率的子图集合。我们把最大的图像放在底部，最小的放在顶部，看起来就像一座金字塔。有两类：高斯金字塔和拉普拉斯金字塔。

import numpy as np
import cv2


img = cv2.imread('./Image/Luffy.jpg')

# cv2.pyrDown从一个高分辨率大尺寸的图像向上构建一个金字塔（尺寸变小，分辨率降低）
lower_reso = cv2.pyrDown(img)

# cv2.pyrUp从一个低分辨率小尺寸的图像向上构建一个金字塔（尺寸变大，但分辨率不会增加）
higher_reso2 = cv2.pyrUp(img)


while(1):
    cv2.imshow('img',img)
    cv2.imshow('lower_reso',lower_reso)
    cv2.imshow('higher_reso2', higher_reso2)
    if cv2.waitKey() == ord('q'):
        break
cv2.destroyAllWindows()






