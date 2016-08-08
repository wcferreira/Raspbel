#!/usr/bin/python

# -*- coding: utf-8 -*-
import binascii
import serial
import time
import sys

# Serial Port Configuration
#print("Configurando serial...")
ser = serial.Serial(
	port = "/dev/ttyUSB0",
	baudrate = 230400,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 5
)

payload_rx = ser.read()
while payload_rx is not None:
    payload_rx = ser.read()
    print '%x' % ord(payload_rx)
ser.close()

