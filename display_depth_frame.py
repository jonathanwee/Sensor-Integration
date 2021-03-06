#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from openni import openni2
import platform
import numpy as np
import cv2
import time


# Initialize OpenNI
if platform.system() == "Windows":
    openni2.initialize("C:/Program Files/OpenNI2/Redist")  # Specify path for Redist
else:
    openni2.initialize()  # can also accept the path of the OpenNI redistribution

# Connect and open device
dev = openni2.Device.open_any()

# Create depth stream
depth_stream = dev.create_depth_stream()
depth_stream.start()

cv2.namedWindow("Depth View", cv2.WINDOW_NORMAL)

while cv2.waitKey(1) == -1 and cv2.getWindowProperty("Depth View", cv2.WND_PROP_FULLSCREEN) != -1:
    frame = depth_stream.read_frame()
    frame_data = frame.get_buffer_as_uint16()
    depth_array = np.asarray(frame_data).reshape((60, 80))

    # Trimming depth_array
    max_distance = 1000 # tweak this
    min_distance = 0
    out_of_range = depth_array > max_distance
    too_close_range = depth_array < min_distance
    depth_array[out_of_range] = max_distance
    depth_array[too_close_range] = min_distance

    # Scaling depth array
    depth_scale_factor = 600.0 / (max_distance - min_distance) #Tweak this
    depth_scale_offset = -(min_distance * depth_scale_factor)
    depth_array_norm = depth_array * depth_scale_factor + depth_scale_offset

    rgb_frame = cv2.applyColorMap(depth_array_norm.astype(np.uint8), cv2.COLORMAP_RAINBOW) #pick colour map

    # Replacing invalid pixel by black color
    rgb_frame[np.where(depth_array == 0)] = [0, 0, 0]

    # Display image
    rgb_frame = cv2.resize(rgb_frame, (800, 600), interpolation=cv2.INTER_AREA)
    cv2.imshow("Depth View", rgb_frame)
    cv2.imwrite('Savedimg.jpg', rgb_frame)
    time.sleep(3)

    #image save
#    vidcap = cv2.VideoCapture(rgb_frame)  
#    while True:
            # Capture frame-by-frame
 #           ret, frame = vidcap.read()

            # Display the resulting frame
  #          cv2.imshow('Video', frame)

   #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #            break  
     # When everything is done, release the capture
    #vidcap.release()
    #cv2.destroyAllWindows() 



depth_stream.stop()
openni2.unload()