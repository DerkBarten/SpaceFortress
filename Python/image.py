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

def onclick(event):
    global mode
    global image
    if event.xdata != None and event.ydata != None:
        if mode == con.MODE.TO_POINT:
	    print distance_y(con.IMAGE_HEIGHT - event.ydata)
	if mode == con.MODE.TO_OBJECT and segments is not None:
	    x = int(event.xdata)
	    y = int(event.ydata)
	    print segments.item((y,x))
	    c = plt.gca()
	    c.imshow(image)
	    plt.show()
	else: 
	    print "shae"



def slic_segmentation(image_path):
  global segments
  global image
  image = io.imread(image_path)
  segments = slic(image, n_segments=con.N_SEGMENTS, compactness=con.COMPACTNESS, sigma=con.SIGMA)
  plot_image(segments)

if __name__ == '__main__':
  fig = plt.gcf()
  fig.canvas.mpl_connect('button_press_event', onclick)
  slic_segmentation("/home/derk/Projects/Sumo_Project/Own_Code/DataPoints/100.jpg")
  
  #from skimage import data, io, filters, color
  #from scipy import ndimage as ndi
  #from skimage.feature import canny
  

  
  #image = color.rgb2gray(image)
  #edges = filters.sobel(image)
  #edges = canny(image)
  
  ##filled = ndi.binary_fill_holes(edges)
  #io.imshow(edges)
  ##io.imshow(image)
  #io.show()
  ##plot_image("/home/derk/Projects/Sumo_Project/Own_Code/DataPoints/100.jpg")
  
  