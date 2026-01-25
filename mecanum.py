import pca9685
from machine import I2C

i2c = I2C(2)
pca = pca9685.PCA9685(i2c)
pca.set_frequency(50)



def front_right(speed):
    if speed > 0:
        pca.pwm(0, 4095)
        pca.pwm(1, 4095 - speed)
    else:
        pca.pwm(0, 4095 + speed)
        pca.pwm(1, 4095)

def front_left(speed):
    if speed > 0:
        pca.pwm(2, 4095)
        pca.pwm(3, 4095 - speed)
    else:
        pca.pwm(2, 4095 + speed)
        pca.pwm(3, 4095)

def back_right(speed):
    if speed > 0:
        pca.pwm(5, 4095)
        pca.pwm(4, 4095 - speed)
    else:
        pca.pwm(5, 4095 + speed)
        pca.pwm(4, 4095)

def back_left(speed):
    if speed > 0:
        pca.pwm(7, 4095)
        pca.pwm(6, 4095 - speed)
    else:
        pca.pwm(7, 4095 + speed)
        pca.pwm(6, 4095)

def drive(x, y, r):
    v14 = 1 / 2**0.5 * (y + x)
    v14y = v14 / 2**0.5
    v23 = 2**0.5 * (y - v14y)
    front_left(v14 - r)
    back_right(v14 + r)
    front_right(v23 + r)
    back_left(v23 - r)

def arm(angle):
    if angle > 170:
        angle = 170
    elif angle < 0:
        angle = 0
    pca.servo_deg(14, angle)

def claw_open():
    pca.servo_deg(15, 170)

def claw_close():
    pca.servo_deg(15, 90)


