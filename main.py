import mecanum
import line_camera as camera
import time

X_GAIN = 4000
R_GAIN = 70

while True:
    cblob_offset, angle, turn180 = camera.get_line()
    x = cblob_offset * X_GAIN
    y = 500
    r = angle * R_GAIN


    print(x, y, r)
    if turn180:
        stop_time = time.ticks_ms() + 1500
        while stop_time > time.ticks_ms():
            mecanum.drive(0, 0, 2000)
        break
    else:
        mecanum.drive(x, y, r)

mecanum.drive(0,0,0)
