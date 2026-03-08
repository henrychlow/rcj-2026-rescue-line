import mecanum
import line_camera as camera
import time
import vl53l0x
from machine import I2C

X_GAIN = 4000
R_GAIN = 70

i2c = I2C(2)
mecanum.init(i2c)

dist_sensor = vl53l0x.VL53L0X(i2c, addr=41)
dist_sensor.start()

# while True:
#     print(vl53l0x_device.read())
#     time.sleep(1)

ignore_time = 0 # ignore double green time

while True:
    cblob_offset, angle, turn180, double_black = camera.get_line()
    x = cblob_offset * X_GAIN
    y = 500
    r = angle * R_GAIN

    print(x, y, r)
    if turn180 and time.ticks_ms() > ignore_time:
        stop_time = time.ticks_ms() + 1500
        while stop_time > time.ticks_ms():
            mecanum.drive(0, 0, 2000)
        ignore_time = time.ticks_ms() + 2000
    elif 0 < dist_sensor.read() <= 120:
        mecanum.drive(1500, 0, 400)
        while cblob_offset != 0: # turn until no line
            cblob_offset, angle, turn180, double_black = camera.get_line()
            print(cblob_offset)
            pass
        while cblob_offset <= 0: # turn until see line
            cblob_offset, angle, turn180, double_black = camera.get_line()
            print(cblob_offset)
            # print('abc')
        stop_time = time.ticks_ms() + 1500
        while stop_time > time.ticks_ms(): # turn 180 deg
            mecanum.drive(0, 0, 2000)
    else:
        mecanum.drive(x, y, r)

    if double_black:
        ignore_time = time.ticks_ms() + 2000



    # while cblob_offset != 0: # wait until no line
    #     cblob_offset, angle, turn180, double_black = camera.get_line()
    #     print(cblob_offset)
    #     pass
    # # print('abc123')
    # while cblob_offset <= 0:
    #     cblob_offset, angle, turn180, double_black = camera.get_line()
    #     print(cblob_offset)
    # # print('abc')
    # distance = dist_sensor.read()
    # if 0 < distance <= 120:
    #     stop_time = time.ticks_ms() + 1500
    #     while stop_time > time.ticks_ms():
    #         mecanum.drive(0, 0, 2000)

mecanum.drive(0,0,0)
