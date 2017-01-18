from Naked.toolshed.shell import execute_js
import time


def forward(distance):
    T_STOP_FORWARD = 0.19
    V_AVG = 56.1836503563
    MIN_RUNTIME = 0.10
    # fake grass
    TRACTION_MODIFIER=1.0778
    TRACTION_MODIFIER=1.0
    forward_time = (distance / V_AVG - T_STOP_FORWARD)*1000 * TRACTION_MODIFIER
    print forward_time
    if forward_time > MIN_RUNTIME: 
        execute_js('forward', str(forward_time))

# minimal angle is 30
def rotate(angle):
    # time 50 gives 30
    if(abs(angle) < 30):
        print "invalid angle"
        return
    
    #T_BASIS = 335
    T_BASIS = 62
    #T_STOP_ROTATE = 490 
    T_STOP_ROTATE = 490
    
    left_rotation = angle < 0
    angle = abs(angle)
    multiplier = float(angle) / 30.0
    print multiplier
    #rotation_time = multiplier * T_BASIS + (multiplier - 1) * T_STOP_ROTATE
    rotation_time = T_BASIS * multiplier + (multiplier - 1) * T_STOP_ROTATE
    if rotation_time < 1:
        rotation_time = T_BASIS
    
    if left_rotation:
        rotation_time *= -1
    #rotation_time = 3200
    print rotation_time
    execute_js('rotate', str(rotation_time)) # needs to be passed as a string

# in miliseconds
def wait(time):
    execute_js('wait', str(time))

# DEPRECATED
def r180():
    rotate(90)
    time.sleep(0.5)
    rotate(90)

def square(radius):
    i = 0
    for i in range(0,4):
        forward(radius)
        time.sleep(0.5)
        rotate(-90)
        time.sleep(0.5)
        i+=1
        
def line(length):
    forward(length)
    time.sleep(0.5)
    r180()
    time.sleep(0.5)
    forward(length)
    time.sleep(0.5)
    r180()
    time.sleep(0.5)
    
def jump():
    execute_js('jump')
    time.sleep(0.5)
