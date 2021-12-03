import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib
import time

HOST='192.168.3.6'
PORT=3988


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.setblocking(False)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(60)
print('Socket now listening')

conn,addr=s.accept()

data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
while True:
    while len(data) < payload_size:
        print("Recv: {}".format(len(data)))
        data += conn.recv(512)


    print("Done Recv: {}".format(len(data)))
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    print("msg_size: {}".format(msg_size))
    # print(struct.unpack('>L',packed_msg_size)[0])
    while len(data) < msg_size:
        data += conn.recv(msg_size//100)
    frame_data = data[:msg_size]
    data = data[msg_size:]


    frame_rgb,frame_depth=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame_rgb = cv2.imdecode(frame_rgb, cv2.IMREAD_COLOR)

    # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(frame_depth, alpha=0.03), cv2.COLORMAP_BONE)

    depth_colormap_dim = depth_colormap.shape
    color_colormap_dim = frame_rgb.shape

    # If depth and color resolutions are different, resize color image to match depth image for display
    if depth_colormap_dim != color_colormap_dim:
        resized_color_image = cv2.resize(frame_rgb, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]),
                                         interpolation=cv2.INTER_AREA)
        images = np.hstack((resized_color_image, depth_colormap))
    else:
        images = np.hstack((frame_rgb, depth_colormap))

    # Show images
    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('RealSense', images)


    cv2.waitKey(1)