from hcsr04 import HCSR04
from machine import Pin
import time

# affectation des pin au capteur sonore HCSR04
sensor = HCSR04(trigger_pin=5,echo_pin=18,echo_timeout_us=1000000)

def read_distance():
    distance = sensor.distance_cm()
    newDistance = distance
    print(distance, 'cm')
    return distance 

def print_distance():
    distance = sensor.distance_cm()
    print(distance,' cm')
