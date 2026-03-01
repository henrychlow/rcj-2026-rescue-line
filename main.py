import mecanum
import line_camera as camera
import time
import vl53l0x
from machine import I2C

X_GAIN = 4000
R_GAIN = 70

i2c = I2C(2)
mecanum.init(i2c)

# dist_sensor = vl53l0x.VL53L0X(i2c, addr=41)
# dist_sensor.start()

ignore_time = 0

while True:
    cblob_offset, angle, turn180, double_black = camera.get_line()
    x = cblob_offset * X_GAIN
    y = 500
    r = angle * R_GAIN

    # print(x, y, r)
    # if turn180 and time.ticks_ms() > ignore_time:
    #     stop_time = time.ticks_ms() + 1500
    #     while stop_time > time.ticks_ms():
    #         mecanum.drive(0, 0, 2000)
    #     ignore_time = time.ticks_ms() + 2000
    # else:
    #     mecanum.drive(x, y, r)

    # if double_black:
    #     ignore_time = time.ticks_ms() + 2000
    # if 0 < dist_sensor.read() < 200:

    mecanum.drive(1500, 0, 400)

    while cblob_offset != 0: # wait until no line
        cblob_offset, angle, turn180, double_black = camera.get_line()
        print(cblob_offset)
        pass
    print('abc123')
    while cblob_offset <= 0:
        cblob_offset, angle, turn180, double_black = camera.get_line()
        print(cblob_offset)
    print('abc')
    stop_time = time.ticks_ms() + 1500
    while stop_time > time.ticks_ms():
        mecanum.drive(0, 0, 2000)
    break

mecanum.drive(0,0,0)
