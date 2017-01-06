# CONSTANTS OF NAVGATION.PY
MINIMAL_SPEED=20
DISTANCE_CONSTANT=2.75
STOP_CONSTANT=0.4
BASIC_TURNSPEED=0.125


# CONSTANTS OF IMAGE.PY

# constants found by fitting the data to the curve
A=33.1
B=0.089

# image received from the robot
IMAGE_HEIGHT = 480
IMAGE_WIDTH=640

# the horizon in the image, assuming the camera is in a 90 degree angle to the ground, 
# it is half of the image height
HORIZON= IMAGE_HEIGHT / 2

# the distance of the lowest pixel in the screen
BOTTOM_OF_SCREEN=17
