## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2015-2017 Intel Corporation. All Rights Reserved.

###############################################
##      Open CV and Numpy integration        ##
###############################################

import pyrealsense2 as rs
import numpy as np
import cv2
import socket
import io
import struct
import time
import pickle
import zlib

address = ('192.168.3.247', 3987)



# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()

# Get device product line for setting a supporting resolution
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))

found_rgb = False
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        break
if not found_rgb:
    print("The demo requires Depth camera with Color sensor")
    exit(0)

config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

# Start streaming
pipeline.start(config)
align = rs.align(rs.stream.color)
connect2server=False
while not connect2server:
    try:

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(address)
        connection = client_socket.makefile('wb')
        print('[Server connected!]')
        break
    except ConnectionRefusedError or ConnectionResetError:
        print('[Finding Server...]')
        time.sleep(2)
        continue
try:



    while True:

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        frames = align.process(frames)
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        result_color, color_image = cv2.imencode('.jpg', color_image, encode_param)
        #result_depth, depth_image = cv2.imencode('.jpg', depth_image, encode_param)

        push = [color_image,depth_image]
        data = pickle.dumps(push, 0)
        size = len(data)
        # print(struct.pack(">L", size))


        try:
            client_socket.sendall(struct.pack(">L", size) + data)
        except:
            print('[Connection fail reconnecting...]')
            try:
                time.sleep(5)
                client_socket.close()
                time.sleep(1)
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(address)
                connection = client_socket.makefile('wb')
                print('[Reconnected!]')

            except:
                print('[Reconnecting in 5s...]')
                time.sleep(5)
        cv2.waitKey(1)


finally:

    # Stop streaming

    pipeline.stop()
