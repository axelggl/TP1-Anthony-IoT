# Students : Axel Maerten, Théau Yapi, Dorian Blatière
import time
from motors import Motor
from captor import *
from machine import Timer

#C reation of the left motor and the right motor
left_wheel = Motor(14, 12, 13)
right_wheel = Motor(25, 26, 33) # Parameters 25 and 26 are the physical pins for the way, 33 is the physical pin for the speed


"""
Every function created
"""

def forward_fullspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go forward at full speed
    """
    if read_distance() > 10:
        left_wheel.forward_fullspeed_motor()
        right_wheel.forward_fullspeed_motor()
    else:
        stop_vehicle(left_wheel, right_wheel)

def forward_halfspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go forward at half speed
    """
    if read_distance() > 10:
        left_wheel.forward_halfspeed_motor()
        right_wheel.forward_halfspeed_motor()
    else:
        stop_vehicle(left_wheel, right_wheel)

def forward_lowspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go forward at low speed
    """
    if read_distance() > 10:
        left_wheel.forward_lowspeed_motor()
        right_wheel.forward_lowspeed_motor()
    else:
        stop_vehicle(left_wheel, right_wheel)

def backward_fullspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go backward at full speed
    """
    if read_distance() > 10:
        left_wheel.backward_fullspeed_motor()
        right_wheel.backward_fullspeed_motor()
    else:
        stop_vehicle(left_wheel, right_wheel)

def backward_halfspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go backward at half speed
    """
    if read_distance() > 10:
        left_wheel.backward_halfspeed_motor()
        right_wheel.backward_halfspeed_motor()
    else:
        stop_vehicle(left_wheel, right_wheel)

def backward_lowspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go backward at low speed
    """
    if read_distance() > 10:
        left_wheel.backward_lowspeed_motor()
        right_wheel.backward_lowspeed_motor()
    else:
        stop_vehicle(left_wheel, right_wheel)

def turn_left(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) turn to the left
    """
    if read_distance() > 10:
        left_wheel.release()
        right_wheel.forward_fullspeed_motor()
    else:
        stop_vehicle(left_wheel, right_wheel)
    
def turn_right(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) turn to the right
    """
    if read_distance() > 10:
        left_wheel.forward_fullspeed_motor()
        right_wheel.release()
    else:
        stop_vehicle(left_wheel, right_wheel)

def stop_vehicle(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) stop
    """
    left_wheel.stop()
    right_wheel.stop()


"""
Tests every function created
"""
while True:
    
#    while read_distance() >= 10:

    forward_fullspeed(left_wheel, right_wheel) # goes forward at full speed
    time.sleep(2)                              # does it for 2 seconds
    
    forward_halfspeed(left_wheel, right_wheel) # goes forward at "half" speed
    time.sleep(2)                              # does it for 2 seconds
    
    forward_lowspeed(left_wheel, right_wheel)  # goes forward at low speed
    time.sleep(2)                              # does it for 2 seconds
    

    backward_fullspeed(left_wheel, right_wheel) # goes backwards at full speed
    time.sleep(2)                               # does it for 2 seconds
    
    backward_halfspeed(left_wheel, right_wheel) # goes backwards at "half" speed
    time.sleep(2)                               # does it for 2 seconds
     
    backward_lowspeed(left_wheel, right_wheel)	# goes backwards at low speed
    time.sleep(2)                             	# does it for 2 seconds

    turn_left(left_wheel, right_wheel)			# goes left at full speed
    time.sleep(2)								# does it for 2 seconds

    turn_right(left_wheel, right_wheel)			# goes right at full speed
    time.sleep(2)								# does it for 2 seconds
        
    stop_vehicle(left_wheel, right_wheel)			# vehicle stopped
        
    
