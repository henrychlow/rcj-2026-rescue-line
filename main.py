import mecanum
import line_camera as camera

while True:
    cblob_offset, angle = camera.get_line()
    x = cblob_offset * 1
    y = 1000
    r = angle * 1
    mecanum.drive(x, y, r)
