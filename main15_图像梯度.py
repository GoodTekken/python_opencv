# https://www.kancloud.cn/aollo/aolloopencv/271601


import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('./Image/Luffy.jpg',0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img[:,::-1],cmap='gray')
plt.title('original'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian[:,::-1],cmap='gray')
plt.title('laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx[:,::-1],cmap='gray')
plt.title('Sobel X'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely[:,::-1],cmap='gray')
plt.title('Sobel Y'),plt.xticks([]),plt.yticks([])

plt.show()




