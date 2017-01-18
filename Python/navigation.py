from sumopy.interface import SumoController
import constants as con
import math

# def move(self, speed, turn=0, duration=1.0, block=True):
#controller = SumoController()

# we take a constant speed of 10, for now
#controller.move(40,0,2)
   



def move_to_point(delta_x, delta_y, speed, verbose=False):
  if delta_y > 0:
    angle = math.degrees(math.tan(float(delta_x) / float(delta_y)))
    path_length = delta_y#get_path_length(delta_x, delta_y)
    duration = get_duration(speed, path_length)
    angle_per_sec = float(angle) / float(duration)
    turn_speed = get_turnspeed(angle_per_sec)
    
    controller = SumoController()
    controller.move(speed, 0, duration)
    
    if verbose:
      print "Pathlenght = " + str(path_length)
      print "Duration = " + str(duration)
      print "Speed = " + str(speed)
      print "Angle(degrees) = " + str(angle)
      print "Turnspeed = " + str(turn_speed)
  
def turn(angle, speed):
    return true

# This should roughly give the correct distance
def get_distance(speed, time):
  return (speed * con.DISTANCE_CONSTANT) * time + speed * con.STOP_CONSTANT

# This is a rewrite of the above formula
def get_duration(speed, distance):
  return float(distance - (speed * con.STOP_CONSTANT)) / float(speed * con.DISTANCE_CONSTANT)


def circle_radius(delta_x, delta_y):
  return math.sqrt((float(delta_x**2) + float(delta_y**2))/2.0)

# TODO not so sure about this
def get_path_length(delta_x, delta_y):
  radius = circle_radius(delta_x, delta_y)
  # we use a 90 degree angle, so we always have one quarter of the circle
  return 0.25 * 2 * math.pi * radius

def get_turnspeed(angle_per_sec):
  return con.BASIC_TURNSPEED * angle_per_sec

def picture(controller, name):
  controller.store_pic()
  pic = controller.get_pic()
  with open(name, 'wb') as f:
    f.write(controller.get_pic())

  #print circle_radius(6.2,2.5)
  #print duration(20,63)
  #move_to_point(0,50,30)
  #move_to_point(0,50,30)
  
