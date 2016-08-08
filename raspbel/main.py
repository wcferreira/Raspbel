#!/usr/bin/python3

# -*- coding: utf-8 -*-
from statemachine import *
import serial

if __name__ == "__main__":
	ser = serial.Serial(
		port = "/dev/ttyUSB0",
		baudrate = 230400,
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE,
		bytesize = serial.EIGHTBITS,
		timeout = 5
	)

	fsm = StateMachine()
	while True:
		try:
			byte = ord(ser.read(1))
			fsm.run(byte)
		except KeyboardInterrupt:
			print('Bye')
			ser.close()
			sys.exit()
