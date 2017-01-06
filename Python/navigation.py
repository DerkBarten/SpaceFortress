from sumopy.interface import SumoController
import constants as c
import math

# def move(self, speed, turn=0, duration=1.0, block=True):
#controller = SumoController()

# we take a constant speed of 10, for now
#controller.move(40,0,2)
   



def move_to_point(delta_x, delta_y, speed):
  if delta_y > 0:
    angle = math.degrees(math.tan(float(delta_x) / float(delta_y)))
    path_length = get_path_length(delta_x, delta_y)
    duration = get_duration(speed, path_length)
    angle_per_sec = float(angle) / float(duration)
    turn_speed = get_turnspeed(angle_per_sec)
    
    print "Pathlenght = " + str(path_length)
    print "Duration = " + str(duration)
    print "Angle(degrees) = " + str(angle)
    print "Turnspeed = " + str(turn_speed)
  
  

# This should roughly give the correct distance
def get_distance(speed, time):
  return (speed * c.DISTANCE_CONSTANT) * time + speed * c.STOP_CONSTANT

# This is a rewrite of the above formula
def get_duration(speed, distance):
  return float(distance - (speed * c.STOP_CONSTANT)) / float(speed * c.DISTANCE_CONSTANT)


def circle_radius(delta_x, delta_y):
  return math.sqrt((float(delta_x**2) + float(delta_y**2))/2.0)


def get_path_length(delta_x, delta_y):
  radius = circle_radius(delta_x, delta_y)
  # we use a 90 degree angle, so we always have one quarter of the circle
  return 0.25 * 2 * math.pi * radius

def get_turnspeed(angle_per_sec):
  return c.BASIC_TURNSPEED * angle_per_sec

  
# lets measure the rotation in degrees per second
# turnspeed	degrees/second
# 22-23		180 +- (little more, little less) pi
# 45		360 +- 2pi
# 90		720 (precise) 4pi

# lets measure distance

# speed duration distance (y = 55t + 8?)
# 20	1	63
# 20    2       118
# 20	3	174

# 40	1	125 (2x stop distance?)
# 40	2	220 (probably because low battery a bit low)

#print circle_radius(6.2,2.5)
#print duration(20,63)
move_to_point(200,200,60)


