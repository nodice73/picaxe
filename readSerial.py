#!/usr/bin/env/ python

from serial import *
import sys

serial_port = "/dev/ttyUSB0"
baud_rate = 4800
ser = Serial(serial_port, baud_rate, timeout=0, writeTimeout=0)

while True:
    c = ser.readline()
    if c == '\r' or c == 0:
        c = ''
    sys.stdout.write(c)
    sys.stdout.flush()
