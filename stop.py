import mecanum
from machine import I2C

i2c = I2C(2)
mecanum.init(i2c)

mecanum.front_left(0)
mecanum.front_right(0)
mecanum.back_left(0)
mecanum.back_right(0)
