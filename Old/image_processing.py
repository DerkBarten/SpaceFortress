import matplotlib.pyplot as plt
import math

from node_sumo import forward
""" Parrot Jumping Sumo frame grabber.

From: http://www.thisismyrobot.com/2015/09/capturing-photos-from-parrot-jumping.html
"""
import base64
import socket
import telnetlib
import time
import socket
from StringIO import StringIO
from matplotlib.image import imread
from matplotlib import pyplot as plt

PARROT_IP = '192.168.2.1'

fig = plt.gcf()
SNAPSHOT_HEIGHT = 240
MAX_DISTANCE = 400

HORIZON_Y=SNAPSHOT_HEIGHT/2# asuming the angle between camera and ground is zero
DISTANCE_BOTTOM=19 #TODO real value
CONSTANT=HORIZON_Y * DISTANCE_BOTTOM * -1

def snapshot(ip_addr, width=160, height=120, timeout=3):
    """ Returns raw JPEG data from Parrot jumping sumo.
    """
    # Connect to the sumo and request the image
    try:
        tconn = telnetlib.Telnet(ip_addr, timeout=timeout)
        tconn.read_until('[JS] $ ')
        tconn.write('kill `pidof dragon-prog`\r\n')
        tconn.read_until('[JS] $ ')
        tconn.write(
            ' '.join((
                'echo \'\' > /dev/stdout',
                ';',
                'yavta',
                '--skip=1',
                '-s{}x{}'.format(width, height),
                '-c2',
                '-F/dev/stdout',
                '-fMJPEG',
                '/dev/video0',
                '> /dev/null',
                ';',
                'base64 /dev/stdout',
            )) + '\r\n'
        )
        
    except socket.timeout:
        raise Exception('Failed to connect to Jumping Sumo and request image.')

    res = tconn.read_until(
        '[JS] $ '
    ).split('base64 /dev/stdout')[1].replace('\r\n', '')[:-7]
    tconn.close()
    return base64.b64decode(res)[1:]

    
def run():
    shot = snapshot(PARROT_IP,400,400,1)
    buffer = StringIO(shot)
    im = imread(buffer, format = 'jpeg')
    plot_image(im)
    


def load_image(name):
    return plt.imread(name)



def get_color(x,y, image):
    return image[y][x]



def plot_image(image):
    global fig
    ax = plt.gca()
    implot = ax.imshow(image)
    
    plt.show()

# DEPRICATED
def pixel_y_to_distance(y):
    A = 0.000000000000001
    B = 0.40376
    C = 0.0053093
    D = 6.167
    return A * math.pow(math.e,y*B)+C*y**2+D

# NEED MORE DATA FROM POINTS FAR AWAY
def y_distance(pixels):
    print "pixels " + str(pixels)
    #return CONSTANT / (y-HORIZON_Y)
    DISTANCE_BOTTOM=17.3
    HORIZON_Y=102
    t = math.tan(pixels/ (HORIZON_Y / (math.pi /2.0)))
    return (t/0.083)+DISTANCE_BOTTOM
    
def onclick(event):
    global image
    if event.xdata != None and event.ydata != None:
        r = y_distance(SNAPSHOT_HEIGHT - event.ydata)
        print r
        #print get_color(int(round(event.xdata,0)), int(round(event.ydata,0)), image)
        
cid = fig.canvas.mpl_connect('button_press_event', onclick)
#run()


image = load_image('figure_1.png')
plot_image(image)


# data points 10 cm between points
# d1 = 3000 - 2170 = 830 
# d2 = 2170 - 1890 = 280
# d3 = 1890 - 1710 = 180
# d4 = 1710 - 1610 = 100
# d5 = 1610 - 1530 = 80
# d6 = 1530 - 1475 = 55

#830
#1110
#1290
#1390
#1470
#1525
# probably something like 1/x



# sample taken with mobile phone, table not 100% flat; not very accurate

# http://stackoverflow.com/questions/15721094/detecting-mouse-event-in-an-image-with-matplotlib

# maybe this?
# http://www.pyimagesearch.com/2015/01/19/find-distance-camera-objectmarker-using-python-opencv/
# http://stackoverflow.com/questions/15670351/how-to-calculate-a-specific-distance-inside-of-a-picture



# 320x240

# DATA
# 698 - 661 = 37 px,  10 cm         % 12.722063037
# 698 - 536 = 162 px, 20 cm         % 55.702005731
# 698 - 469 = 229 px, 30 cm         % 78.739255014
# 698 - 455 = 243 px, 40 cm         83.553008596
# 698 - 445 = 253 px, 50 cm         86.991404011

# exponential regression gives: y\ =\ 6.525542096\cdot e^{0.02184783752x}


# https://www.desmos.com/calculator/jwquvmikhr

