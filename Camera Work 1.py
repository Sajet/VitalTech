# Author: Tejas Madhavan
# Date: Mar 27 2017
# Version: 1.0

# This is a script that does basic camera work :D

# Websites:
# https://www.element14.com/community/community/raspberry-pi/raspberry-pi-accessories/blog/2015/06/25/getting-to-know-the-raspberry-pi-camera-and-pi-noir
# https://www.raspberrypi.org/documentation/usage/camera/python/README.md
# http://stackoverflow.com/questions/23183976/recording-video-from-raspberry-pi-and-saving-it-to-a-external-hard-drive

# How to mess with different comands:
# https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/

# PiCamra documentation
# http://picamera.readthedocs.io/en/release-1.13/

# Libraries
import time
import picamera
import os
camera = picamera.PiCamera()

rt = 5

print('start')

# This opens a preview and starts recording
camera.start_preview()
# camera.add_overlay()
camera.start_recording('video1.h264') #Be sure video file name is matched below!!!

# Record for rt amount of time
time.sleep(rt)

# This stops the recording and stops the preview
camera.stop_recording()
camera.stop_preview()
camera.close()

print('end')

# This plays the recorded video through omxplayer through the os command window
os.system('omxplayer video1.h264')
