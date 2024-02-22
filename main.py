#Students : Axel Maerten, Théau Yapi, Dorian Blatière
import time
from motors import Motor

#Creation of the left motor and the right motor
left_wheel = Motor(14, 12, 13)
right_wheel = Motor(25, 26, 33) # Parameters 25 and 26 are the physical pins for the way, 33 is the physical pin for the speed


"""

"""
def forward_fullspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go forward at full speed
    """
    left_wheel.forward_fullspeed_motor()
    right_wheel.forward_fullspeed_motor()

def forward_halfspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go forward at half speed
    """
    left_wheel.forward_halfspeed_motor()
    right_wheel.forward_halfspeed_motor()

def forward_lowspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go forward at low speed
    """
    left_wheel.forward_lowspeed_motor()
    right_wheel.forward_lowspeed_motor()

def backward_fullspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go backward at full speed
    """
    left_wheel.backward_fullspeed_motor()
    right_wheel.backward_fullspeed_motor()

def backward_halfspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go backward at half speed
    """
    left_wheel.backward_halfspeed_motor()
    right_wheel.backward_halfspeed_motor()

def backward_lowspeed(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) go backward at low speed
    """
    left_wheel.backward_lowspeed_motor()
    right_wheel.backward_lowspeed_motor()

def turn_left(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) turn to the left
    """
    left_wheel.release()
    right_wheel.forward_fullspeed_motor()
    
def turn_right(left_wheel, right_wheel):
    """
    Make the vehicle (the two motors) turn to the right
    """
    left_wheel.forward_fullspeed_motor()
    right_wheel.release()

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
    forward_fullspeed(left_wheel, right_wheel)
    time.sleep(2)
    forward_halfspeed(left_wheel, right_wheel)
    time.sleep(2)
    forward_lowspeed(left_wheel, right_wheel)
    time.sleep(2)
    
    backward_fullspeed(left_wheel, right_wheel)
    time.sleep(2)
    backward_halfspeed(left_wheel, right_wheel)
    time.sleep(2)
    backward_lowspeed(left_wheel, right_wheel)
    time.sleep(2)
    
    turn_left(left_wheel, right_wheel)
    time.sleep(2)
    
    turn_right(left_wheel, right_wheel)
    time.sleep(2)
    
    stop_vehicle(left_wheel, right_wheel)
    time.sleep(5)
