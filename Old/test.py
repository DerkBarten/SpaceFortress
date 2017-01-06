#import numpy as np
#import cv2
#from matplotlib import pyplot as plt

#img = cv2.imread('figure_1.png')
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#cv2.imshow('image',thresh)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#import os
#import skimage
#import numpy as np
#from skimage import filters
#from skimage import io
#from skimage.color import rgb2gray
#from skimage.viewer import ImageViewer
#from skimage import segmentation
#from scipy import ndimage
#from skimage.feature import peak_local_max

#camera = io.imread('figure_1.png')
#img_gray = rgb2gray(camera)
#val = filters.threshold_otsu(img_gray)
#mask = img_gray < val



#distance = ndimage.distance_transform_edt(img_gray)
#local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)), labels=img_gray)

## Transform markers image so that 0-valued pixels are to
## be labelled, and -1-valued pixels represent background
#markers = morphology.label(local_maxi)
#markers[~img_gray] = -1
#labels_rw = segmentation.random_walker(img_gray, markers)

#viewer = ImageViewer(labels_rw)
#viewer.show()

import numpy as np
from skimage.morphology import watershed
from skimage.feature import peak_local_max

# Generate an initial image with two overlapping circles
x, y = np.indices((80, 80))
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20
mask_circle1 = (x - x1) ** 2 + (y - y1) ** 2 < r1 ** 2
mask_circle2 = (x - x2) ** 2 + (y - y2) ** 2 < r2 ** 2
image = np.logical_or(mask_circle1, mask_circle2)
# Now we want to separate the two objects in image
# Generate the markers as local maxima of the distance
# to the background
from scipy import ndimage
distance = ndimage.distance_transform_edt(image)
local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)), labels=image)
markers = morphology.label(local_maxi)
labels_ws = watershed(-distance, markers, mask=image)




