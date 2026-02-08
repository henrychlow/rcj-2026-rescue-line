import mecanum
import line_camera as camera

X_GAIN = 4000
R_GAIN = 70

while True:
    cblob_offset, angle = camera.get_line()
    x = cblob_offset * X_GAIN
    y = 500
    r = angle * R_GAIN


    print(x, y, r)
    mecanum.drive(x, y, r)

mecanum.drive(0,0,0)
