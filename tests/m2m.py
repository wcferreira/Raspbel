#!/usr/bin/python3

# -*- coding: utf-8 -*-
from time import sleep
from binascii import hexlify
import serial

def st_get_delimiter():
	print("State: Delimiter")
	if data_rx == 0x7e:
		buffer.insert(index, data_rx)
		return st_get_length_1
	else:
		return st_get_delimiter

def st_get_length_1():
	print("State: Length 1")
	buffer.insert(index, data_rx)
	return st_get_length_2

def st_get_length_2():
	global length
	print("State: Length 2")
	buffer.insert(index, pdata_rx)
	length = int.from_bytes(buffer[1:3], byteorder='big')
	print(length)
	return st_get_data

def st_get_data():
	global cnt
	if  cnt < length:
		print("Count: {}".format(cnt))
		cnt = cnt + 1
		print("State: Frame ID")
		buffer.insert(index, data_rx)
		return st_get_data
	else:
		return None

if __name__ == "__main__":
	ser = serial.Serial(
		port = "/dev/ttyUSB0",
		baudrate = 230400,
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE,
		bytesize = serial.EIGHTBITS,
		timeout = 5
	)

	print(ser.name)
	cnt = 0
	while True:
		data = []
		byte = ser.read(1)
		data.append(byte)
		if byte == b'\x7e':
			cnt = 0
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		if cnt == 110:
			print(data)
		else:
			cnt += 1
		print(hexlify(byte))
	ser.close
