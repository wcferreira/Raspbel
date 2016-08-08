# -*- coding: utf-8 -*-
import serial

class RS232:
	def __init__(self):
		self.ser = serial.Serial(
			port = "/dev/ttyUSB0",
			baudrate = 230400,
			parity = serial.PARITY_NONE,
			stopbits = serial.STOPBITS_ONE,
			bytesize = serial.EIGHTBITS,
			timeout = 5
		)

	def get_data(self):
		return self.ser.read(1)

	def close_serial_port(self):
		self.ser.close()
