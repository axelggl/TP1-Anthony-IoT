from machine import Pin, PWM

class Motor:
    def __init__(self, num_pin_avancer, num_pin_reculer, num_pin_puissance_rotation):
        self.pin_avancer = Pin(num_pin_avancer, Pin.OUT, value=0)
        self.pin_reculer = Pin(num_pin_reculer, Pin.OUT, value=0)
        self.pin_vitesse_rotation = PWM(Pin(num_pin_puissance_rotation), freq=5000, duty_u16=0)
    
    def avancer_100(self, duty_cycle=65535):
        self.pin_avancer.on()
        self.pin_reculer.off()
        self.pin_vitesse_rotation.duty_u16(duty_cycle)
    
    def avancer_50(self, duty_cycle=32768):
        self.pin_avancer.on()
        self.pin_reculer.off()
        self.pin_vitesse_rotation.duty_u16(duty_cycle)
        
    def reculer(self, duty_cycle=65535):
        self.pin_avancer.off()
        self.pin_reculer.on()
        self.pin_vitesse_rotation.duty_u16(duty_cycle)
    
    def stop(self):
        self.pin_avancer.on()
        self.pin_reculer.off()
        self.pin_vitesse_rotation.duty_u16(0)
    
    def libre(self):
        self.pin_avancer.off()
        self.pin_reculer.off()

#p0 = Pin(32, Pin.OUT, value=0)    # create output pin on GPIO0
#p1 = Pin(33, Pin.OUT, value=0)

#p2 = Pin(12, Pin.OUT, value=0)
#p3 = Pin(13, Pin.OUT, value=0)


#pwm2 = PWM(Pin(2), freq=20000, duty=512)
#pwm0 = 25
#pwm1 = 26


