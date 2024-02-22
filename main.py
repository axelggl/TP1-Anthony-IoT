import time
from motors import Motor
from captor import *

roue_droite = Motor(25, 26, 33)
roue_gauche = Motor(14, 12, 13)
    

def avancer_vehicule(roue_droite, roue_gauche):
    roue_droite.avancer_100()
    roue_gauche.avancer_100()
    
def reculer_vehicule(roue_droite, roue_gauche):
    roue_droite.reculer()
    roue_gauche.reculer()
    
def tourner_gauche_vehicule(roue_droite, roue_gauche):
    roue_droite.avancer_100()
    roue_gauche.stop()

def avancer_tourner_gauche_vehicule(roue_droite, roue_gauche):
    roue_droite.avancer_100()
    roue_gauche.avancer_50()

def tourner_droite_vehicule(roue_droite, roue_gauche):
    roue_droite.stop()
    roue_gauche.avancer_100()

def avancer_tourner_droite_vehicule(roue_droite, roue_gauche):
    roue_droite.avancer_50()
    roue_gauche.avancer_100()

def stop_vehicule(roue_droite, roue_gauche):
    roue_droite.stop()
    roue_gauche.stop()

def roues_libres(roue_droite, roue_gauche):
    roue_droite.libre()
    roue_gauche.libre()





while True:
    print_distance()
    
    avancer_vehicule(roue_droite, roue_gauche)
    time.sleep(5)
    
    reculer_vehicule(roue_droite, roue_gauche)
    time.sleep(5)
    
    tourner_gauche_vehicule(roue_droite, roue_gauche)
    time.sleep(5)
    
    tourner_droite_vehicule(roue_droite, roue_gauche)
    time.sleep(5)
    
    avancer_tourner_gauche_vehicule(roue_droite, roue_gauche)
    time.sleep(5)
    
    avancer_tourner_droite_vehicule(roue_droite, roue_gauche)
    time.sleep(5)
    
    roues_libres(roue_droite, roue_gauche)
    time.sleep(5)
    
    stop_vehicule(roue_droite, roue_gauche)
