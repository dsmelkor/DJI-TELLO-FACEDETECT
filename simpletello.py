from djitellopy import Tello
import cv2
import time

tello = Tello()

tello.connect()

tello.get_battery()
tello.get_udp_video_address()
print (tello.get_udp_video_address())
"""
tello.takeoff()
time.sleep(5)

tello.move_left(100)
time.sleep(5)

tello.rotate_counter_clockwise(45)
time.sleep(5)

tello.land()
time.sleep(5)
"""

tello.end()
