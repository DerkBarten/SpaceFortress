from sumopy.interface import SumoController
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io
import numpy as np
import navigation as nav
import constants as con
import image as im # TODO maybe change this name
import time

controller = SumoController()
nav.move_to_point(0, 100, 30, True)
#nav.picture(controller, con.PICTURE_NAME)
#pic = io.imread(con.PICTURE_NAME)


#mode = con.MODE.TO_POINT

#def onclick(event):
  #global mode
  #global image
  #if event.xdata != None and event.ydata != None:
    ##dy =  im.distance_y(con.IMAGE_HEIGHT - event.ydata)
    ##print dy
    #nav.move_to_point(0, 20, con.SPEED)
	
#plt.gcf().canvas.mpl_connect('button_press_event', onclick)
#canvas = plt.gca()
#canvas.imshow(pic)
#canvas.axis('off')
#plt.show()
	    

#print "connected?"