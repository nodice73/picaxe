#!/usr/bin/env/ python

from serial import *
from Tkinter import *
import sys

serial_port = "/dev/ttyUSB0"
baud_rate = 4800
ser = Serial(serial_port, baud_rate, timeout=0, writeTimeout=0)

# make a Tkinter window
root = Tk()
root.wm_title("Reading Serial")

# make a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# make a text box to put the serial output
log = Text(root, width=30, height=30, takefocus=0)
log.pack()

# attach text box to scrollbar
log.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=log.yview)

# make our own buffer
# useful for parsing commands
# Serial.readline seems unreliable at times too
ser_buffer = ""

def readSerial():
    while True:
        global ser_buffer
        c = ser.readline()
        if len(c) == 0:
            break

        if c == '\r':
            c = ''

        if c == '\n':
            ser_buffer += "\n"
            log.insert('0.0', ser_buffer)
            ser_buffer = ""
        else:
            ser_buffer += c

        sys.stdout.write(c)
        sys.stdout.flush()

    root.after(10, readSerial)

root.after(100, readSerial)
root.mainloop()
