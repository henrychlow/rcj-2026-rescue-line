# Untitled - By: Henry - Sun Jan 25 2026

import sensor
import time
import math

# Color Tracking Thresholds (L Min, L Max, A Min, A Max, B Min, B Max)
# The below thresholds track in general red/green things. You may wish to tune them...
thresholds = [
    (0, 5, -7, -2, 0, 5), # black threshold
]

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)  # must be turned off for color tracking
sensor.set_auto_whitebal(False)  # must be turned off for color tracking
clock = time.clock()

# Only blobs that with more pixels than "pixel_threshold" and more area than "area_threshold" are
# returned by "find_blobs" below. Change "pixels_threshold" and "area_threshold" if you change the
# camera resolution. Don't set "merge=True" because that will merge blobs which we don't want here.

def get_line():
    cblob_cx = 160
    ublob_cx = 160
    img = sensor.snapshot()
    black_blobs_center = img.find_blobs(thresholds, pixels_threshold=200, area_threshold=200, roi=(0,90,320,60))
    largest_center_blob_area = 0

    for blob in black_blobs_center:
        # These values depend on the blob not being circular - otherwise they will be shaky.
        if blob.elongation() > 0.5:
            img.draw_edges(blob.min_corners(), color=(255, 0, 0))
            img.draw_line(blob.major_axis_line(), color=(0, 255, 0))
            img.draw_line(blob.minor_axis_line(), color=(0, 0, 255))
        # These values are stable all the time.
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        # Note - the blob rotation is unique to 0-180 only.
        img.draw_keypoints(
            [(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=20
        )

        if blob.area() > largest_center_blob_area:
            largest_center_blob_area = blob.area()
            cblob_cx = blob.cx()

    black_blobs_upper = img.find_blobs(thresholds, pixels_threshold=200, area_threshold=200, roi=(0,0,320,60))
    largest_upper_blob_area = 0

    for blob in black_blobs_upper:
        # These values depend on the blob not being circular - otherwise they will be shaky.
        if blob.elongation() > 0.5:
            img.draw_edges(blob.min_corners(), color=(255, 0, 0))
            img.draw_line(blob.major_axis_line(), color=(0, 255, 0))
            img.draw_line(blob.minor_axis_line(), color=(0, 0, 255))
        # These values are stable all the time.
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        # Note - the blob rotation is unique to 0-180 only.
        img.draw_keypoints(
            [(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=20
        )

        if blob.area() > largest_upper_blob_area:
            largest_upper_blob_area = blob.area()
            ublob_cx = blob.cx()

    cblob_x_offset_pixel = cblob_cx - 160
    cblob_x_offset = (1/160) * cblob_x_offset_pixel

    ublob_x_offset_pixel = ublob_cx - 160

    angle = math.atan2(90, ublob_x_offset_pixel - cblob_x_offset_pixel)

    return cblob_x_offset, angle / math.pi * 180 - 90

while True:
    cblob_offset, angle = get_line()
    print(cblob_offset, angle)
