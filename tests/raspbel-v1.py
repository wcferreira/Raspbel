#!/usr/bin/python3

# -*- coding: utf-8 -*-
import time
from binascii import hexlify
from datetime import datetime
#import serial
import sys
import csv
import os.path
from logbel import *
from dump import *

class BEL:
	NUM_PACS, NUM_SERIE, ID_RADIO, COD_EQUIPAMENTO, ID_CBA, PERSONALIDADE, \
	VERSAO_FW, ESTADO_CEC, ESTADO_CICLO, ESTADO_MAQUINA, DH_PACOTE, VELOCIDADE, \
	HEADING, TAMANHO_IMP, NUM_IMP, LAT, LONG = range(0, 17)

class define:
	DELIMITER = 0x7e
	BEL = 0x07
	FRAME_ID = 0x90
	ESCAPE = 0x7d

def st_get_delimiter():
	print("State: Delimiter")
	if data_rx == define.DELIMITER:
		buffer.insert(index, data_rx)
		return st_get_length_lsb
	else:
		return st_get_delimiter

def st_get_length_lsb():
	global is_escape_char
	print("State: Length LSB")

	byte = data_rx
	if byte == define.ESCAPE:
		print("I've got a escape character")
		is_escape_char = True
		return st_get_length_lsb
	else:
		if is_escape_char == True:
			print("Treating escape character")
			is_escape_char = False
			byte = data_rx ^ 0x20

	if is_escape_char == False:
		buffer.insert(index, byte)
		return st_get_length_msb

def st_get_length_msb():
	global is_escape_char
	global length
	print("State: Length MSB")

	byte = data_rx
	if byte == define.ESCAPE:
		print("I've got a escape character")
		is_escape_char = True
		return st_get_length_msb
	else:
		if is_escape_char == True:
			print("Treating escape character")
			is_escape_char = False
			byte = data_rx ^ 0x20

	if is_escape_char == False:
		buffer.insert(index, data_rx)
		length = int.from_bytes(buffer[1:3], byteorder='big') - 3 # Get rid of CRC (2bytes) and Checksum (1byte)
		print(length)
		return st_get_data

def st_get_data():
	global cnt
	global is_escape_char
	byte = data_rx

	print("Test: {}".format(is_escape_char))

	if  cnt < length:
		print("Count: {}".format(cnt))
		print("State: Frame ID")

		if data_rx == define.ESCAPE:
			print("I've got a escape character")
			is_escape_char = True
		else:
			if is_escape_char == True:
				print("Treating escape character")
				is_escape_char = False
				byte = data_rx ^ 0x20

		if is_escape_char == False:
			buffer.insert(index, byte)
			cnt = cnt + 1

		return st_get_data
	else:
		return get_crc_lsb

def get_crc_lsb():
	global is_escape_char
	print("State: CRC LSB")

	byte = data_rx
	if byte == define.ESCAPE:
		print("I've got a escape character")
		is_escape_char = True
		return get_crc_lsb
	else:
		if is_escape_char == True:
			print("Treating escape character")
			is_escape_char = False
			byte = data_rx ^ 0x20

	if is_escape_char == False:
		buffer.insert(index, byte)
		return get_crc_msb

def get_crc_msb():
	global is_escape_char
	print("State: CRC MSB")

	byte = data_rx
	if byte == define.ESCAPE:
		print("I've got a escape character")
		is_escape_char = True
		return get_crc_msb
	else:
		if is_escape_char == True:
			print("Treating escape character")
			is_escape_char = False
			byte = data_rx ^ 0x20

	if is_escape_char == False:
		buffer.insert(index, byte)
		return get_checksum

def get_checksum():
	global is_escape_char
	print("State: Checksum")

	byte = data_rx
	if byte == define.ESCAPE:
		print("I've got a escape character")
		is_escape_char = True
		return get_checksum
	else:
		if is_escape_char == True:
			print("Treating escape character")
			is_escape_char = False
			byte = data_rx ^ 0x20

	if is_escape_char == False:
		buffer.insert(index, byte)
		dump_bel(buffer)
		print("Writing CSV file ...")
		log_bel(buffer)
		del buffer[:]
		return st_idle

def st_idle():
	return st_idle

if __name__ == "__main__":
#	ser = serial.Serial(
#		port = "/dev/ttyUSB0",
#		baudrate = 230400,
#		parity = serial.PARITY_NONE,
#		stopbits = serial.STOPBITS_ONE,
#		bytesize = serial.EIGHTBITS,
#		timeout = 1
#	)

	payload = [0x7E, 0x00, 0x66, 0x90, 0x00, 0x7D, 0x33, 0xA2, 0x00, 0x40, 0xA6,
               0xE0, 0xEA, 0xFF, 0xFE, 0xC2, 0x01, 0x01, 0x07, 0x00, 0x00, 0x00, 
               0x00, 0x7D, 0x33, 0xA2, 0x00, 0x40, 0xA6, 0xE0, 0xEA, 0x7D, 0x31, 
			   0x38, 0x01, 0xAA, 0xAA, 0xAA, 0x00, 0x00, 0x16, 0xAB, 0xBF, 0x95, 
			   0x00, 0x80, 0x1A, 0x03, 0x01, 0x00, 0xBF, 0x9D, 0xA3, 0x57, 0x33, 
			   0xDD, 0x01, 0x2E, 0x3E, 0x57, 0xDA, 0xBF, 0xDB, 0x8B, 0xCD, 0x1C, 
			   0x09, 0x14, 0xEA, 0xBF, 0xEF, 0xD2, 0x00, 0x00, 0x2E, 0x20, 0x00, 
			   0x00, 0xB2, 0x71, 0xFE, 0xFF, 0xDA, 0x00, 0x00, 0x00, 0x88, 0x7D, 
               0x33, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x31, 0x31, 0x33, 0x38, 
	           0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0xC8, 0xB4, 0x9C]

#	print(ser.name)
	buffer = []
	index = 0
	index_rx = 0
	data_rx = 0
	length = 0
	cnt = 0
	is_escape_char = False
	
#	while True:
	state = st_get_delimiter
	while index < len(payload):
		try:
			data_rx = payload[index]
			state = state()
			#byte = ser.read(1)
			index += 1
		except KeyboardInterrupt:
			print('Bye')
			ser.close()
			sys.exit()

#	ser.close()
	sys.exit()


