#!/bin/bash

sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

cangen vcan0 -g 100 -I 1FE -L 8 -D r
