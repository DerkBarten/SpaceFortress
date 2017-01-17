import math
import constants as con
import navigation as nav
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage import io



mode = con.MODE.TO_OBJECT
segments = None
image = None

def distance_y(pixels):
  # calculate an aproximation of the asymptote
  Asym = float(2 * con.HORIZON) / math.pi
  return (math.tan((pixels + con.A) / Asym) / float(con.B)) + con.BOTTOM_OF_SCREEN

def plot_image(image):
    # in case we just get the path of an image
    canvas = plt.gca()
    canvas.imshow(image)
    canvas.axis('off')
    plt.show()





def slic_segmentation(image_path):
  global segments
  global image
  image = io.imread(image_path)
  segments = slic(image, n_segments=con.N_SEGMENTS, compactness=con.COMPACTNESS, sigma=con.SIGMA)
  plot_image(segments)
