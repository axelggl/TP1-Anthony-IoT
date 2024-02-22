from machine import Pin, PWM

class Motor:
    """
    Motor class
    """
    
    def __init__(self, pin_forward, pin_backward, pin_speed):
        """
        Initialize the forward, backward and pwm pins with the values of the parameters
        
        Parameters :
            pin_forward (int) : number of the pin on the ESP32
            pin_bakcward (int) : number of the pin on the ESP32
            pin_speed (int) : number of the pin on the ESP32
        """
        self.pin_forward = Pin(pin_forward, Pin.OUT, value=0)
        self.pin_backward = Pin(pin_backward, Pin.OUT, value=0)
        self.pwm = PWM(Pin(pin_speed), freq=5000, duty_u16=0)

    #Forward functions
    def forward_fullspeed_motor(self, duty_cycle=65535):
        """
        Make the motor go in the forward way at full speed
        
        Parameters :
            duty_cycle (int) : default value at 65535 which is the 100% speed
        """
        self.pin_forward.on()
        self.pin_backward.off()
        self.pwm.duty_u16(duty_cycle)
        print('Vitesse : ' + str(duty_cycle))
    
    def forward_halfspeed_motor(self, duty_cycle=49151):
        """
        Make the motor go in the forward way at 3/4 speed
        
        Parameter :
            duty_cycle (int) : default value at 49151 which is 75% speed
        """
        self.pin_forward.on()
        self.pin_backward.off()
        self.pwm.duty_u16(duty_cycle)
        print('Vitesse : ' + str(duty_cycle))
    
    def forward_lowspeed_motor(self, duty_cycle=32768):
        """
        Make the motor go in the forward way at low speed (50%)
        
        Parameter :
            duty_cycle (int) : default value at 32768 which is 50% speed
        """
        self.pin_forward.on()
        self.pin_backward.off()
        self.pwm.duty_u16(duty_cycle)
        print('Vitesse : ' + str(duty_cycle))
    
    #Backward functions 
    def backward_fullspeed_motor(self, duty_cycle=65535):
        """
        Make the motor go in the backward way at full speed
        
        Parameter :
            duty_cycle (int) : default value at 65535 which is the 100% speed
        """
        self.pin_forward.off()
        self.pin_backward.on()
        self.pwm.duty_u16(duty_cycle)
        print('Vitesse : ' + str(duty_cycle))
    
    
    def backward_halfspeed_motor(self, duty_cycle=49151):
        """
        Make the motor go in the backward way at 3/4 speed
        
        Parameter :
            duty_cycle (int) : default value at 49151 which is the 75% speed
        """
        self.pin_forward.off()
        self.pin_backward.on()
        self.pwm.duty_u16(duty_cycle)
        print('Vitesse : ' + str(duty_cycle))
        
    def backward_lowspeed_motor(self, duty_cycle=32768):
        """
        Make the motor go in the backward way at low speed (50%)
        
        Parameter :
            duty_cycle (int) : default value at 32768 which is the 50% speed
        """
        self.pin_forward.off()
        self.pin_backward.on()
        self.pwm.duty_u16(duty_cycle)
        print('Vitesse : ' + str(duty_cycle))
    
    def stop(self):
        """
        Make the motor stop and block
        """
        self.pin_forward.on()
        self.pin_backward.on()
        self.pwm.duty_u16(65535)
        print('Vitesse : ' + str(self.pwm.duty_u16))

    def release(self):
        """
        Make the motor stop but free (no force)
        """
        self.pin_forward.off()
        self.pin_backward.off()
        self.pwm.duty_u16(0)
        print('Vitesse : ' + str(self.pwm.duty_u16))
