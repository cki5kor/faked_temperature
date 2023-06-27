#!/bin/python3

from socketcan import CanRawSocket, CanFrame

interface = "vcan0"
s = CanRawSocket(interface=interface)

candata_str = []


while True:
    frame = s.recv()
    candata_str = (['{0:02X}'.format(b) for b in frame.data ])
    candata = candata_str[1] + candata_str[0]
    temp_data = int(candata, 16) 
    temp = 0.001*temp_data
    print(temp)
