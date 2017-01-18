""" Parrot Jumping Sumo frame grabber.

From: http://www.thisismyrobot.com/2015/09/capturing-photos-from-parrot-jumping.html
"""
import base64
import socket
import telnetlib
import time
from StringIO import StringIO
from matplotlib.image import imread
from matplotlib import pyplot as plt

PARROT_IP = '192.168.2.1'
#PARROT_IP = '192.168.2.3'


def snapshot(ip_addr, width=160, height=120, timeout=1):
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

    return base64.b64decode(res)[1:]


if __name__ == '__main__':
    shot = snapshot(PARROT_IP,400,400,200)
    buffer = StringIO(shot)
    im = imread(buffer, format = 'jpeg')
    plt.imshow(im)
    plt.draw()
    plt.show()
