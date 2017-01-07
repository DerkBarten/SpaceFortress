from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np

from skimage.data import astronaut

from skimage.segmentation import felzenszwalb, slic, quickshift
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io, color, filters

img = io.imread("/home/derk/Projects/Sumo_Project/Own_Code/DataPoints/30.jpg")

#segments_fz = felzenszwalb(img, scale=1500, sigma=1, min_size=50)
segments_fz = slic(img, n_segments=45, compactness=14, sigma=3)
print("Felzenszwalb's number of segments: %d" % len(np.unique(segments_fz)))
print(segments_fz)

ax = plt.gca()
#ax.imshow(mark_boundaries(img, segments_fz))
ax.imshow(segments_fz)
ax.set_title("Felzenszwalbs's method")


ax.set_xticks(())
ax.set_yticks(())
plt.show()