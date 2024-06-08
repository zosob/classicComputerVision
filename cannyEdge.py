import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv2.read('edge.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "File could not be found"
edges = cv.Canny(img, 100, 200)

#Plotting the image...
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()