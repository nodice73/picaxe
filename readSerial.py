#!/usr/bin/env/ python

from serial import Serial
import sys

serial_port = "/dev/ttyUSB0"
baud_rate = 4800
ser = Serial(serial_port, baud_rate, timeout=0, writeTimeout=0)

while True:
    c = ser.readline()
    sys.stdout.write(str(c, 'utf-8'))
