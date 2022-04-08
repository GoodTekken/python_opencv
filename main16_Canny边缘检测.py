import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./Image/Luffy.jpg',1)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img[:,:,::-1],cmap='gray')
plt.title('original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges[:,::-1],cmap='gray')
plt.title('edge'),plt.xticks([]),plt.yticks([])

plt.show()