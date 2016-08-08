#!/usr/bin/python3

# -*- coding: utf-8 -*-
import time
import sys
from logbel import *
from dump import *

class Define:
	DELIMITER = 0x7e
	BEL = 0x07
	FRAME_ID = 0x90
	ESCAPE = 0x7d


class StateMachine:
	def __init__(self):
		self.buffer = []
		self.index = 0
		self.data_rx = None
		self.length = 0
		self.cnt = 0
		self.is_escape_char = False
		self.state = self.st_get_delimiter

	def st_get_delimiter(self):
		print("State: Delimiter")
		if self.data_rx == Define.DELIMITER:
			self.buffer.insert(self.index, self.data_rx)
			self.index += 1
			return self.st_get_length_lsb
		else:
			return self.st_get_delimiter

	def st_get_length_lsb(self):
		print("State: Length LSB")

		byte = self.data_rx
		if byte == Define.ESCAPE:
			#print("I've got a escape character")
			self.is_escape_char = True
			return self.st_get_length_lsb
		else:
			if self.is_escape_char == True:
				#print("Treating escape character")
				self.is_escape_char = False
				byte = self.data_rx ^ 0x20

		if self.is_escape_char == False:
			self.buffer.insert(self.index, byte)
			#print("Length LSB: {:02x}".format(byte))
			self.index += 1
			return self.st_get_length_msb

	def st_get_length_msb(self):
		print("State: Length MSB")

		byte = self.data_rx
		if byte == Define.ESCAPE:
			#print("I've got a escape character")
			self.is_escape_char = True
			return self.st_get_length_msb
		else:
			if self.is_escape_char == True:
				#print("Treating escape character")
				self.is_escape_char = False
				byte = self.data_rx ^ 0x20

		if self.is_escape_char == False:
			#print("Length MSB: {:02x}".format(byte))
			self.buffer.insert(self.index, byte)
			self.length = int.from_bytes(self.buffer[1:3], byteorder='big') - 3 # Get rid of CRC (2bytes) and Checksum (1byte)
			#print("Length Parser: {}".format(self.length))
			print(self.buffer)
			self.index += 1
			return self.st_get_data

	def st_get_data(self):
		byte = self.data_rx

		#print("Escape: {}".format(self.is_escape_char))
		#print("@@@ Length @@@: {}".format(self.length))

		if  self.cnt < self.length:
			print("Count: {}".format(self.cnt))
			print("State: Frame ID")

			if self.data_rx == Define.ESCAPE:
				print("I've got a escape character")
				self.is_escape_char = True
			else:
				if self.is_escape_char == True:
					#print("Treating escape character")
					self.is_escape_char = False
					byte = self.data_rx ^ 0x20

			if self.is_escape_char == False:
				self.buffer.insert(self.index, byte)
				self.cnt += 1
				self.index += 1

			return self.st_get_data
		else:
			return self.get_crc_lsb

	def get_crc_lsb(self):
		print("State: CRC LSB")

		byte = self.data_rx
		if byte == Define.ESCAPE:
			#print("I've got a escape character")
			self.is_escape_char = True
			return self.get_crc_lsb
		else:
			if self.is_escape_char == True:
				#print("Treating escape character")
				self.is_escape_char = False
				byte = self.data_rx ^ 0x20

		if self.is_escape_char == False:
			self.buffer.insert(self.index, byte)
			self.index += 1
			return self.get_crc_msb

	def get_crc_msb(self):
		print("State: CRC MSB")

		byte = self.data_rx
		if byte == Define.ESCAPE:
			#print("I've got a escape character")
			self.is_escape_char = True
			return self.get_crc_msb
		else:
			if self.is_escape_char == True:
				#print("Treating escape character")
				self.is_escape_char = False
				byte = self.data_rx ^ 0x20

		if self.is_escape_char == False:
			self.buffer.insert(self.index, byte)
			self.index += 1
			return self.get_checksum

	def get_checksum(self):
		print("State: Checksum")

		byte = self.data_rx
		if byte == Define.ESCAPE:
			#print("I've got a escape character")
			self.is_escape_char = True
			return self.get_checksum
		else:
			if self.is_escape_char == True:
				#print("Treating escape character")
				self.is_escape_char = False
				byte = self.data_rx ^ 0x20

		if self.is_escape_char == False:
			self.buffer.insert(self.index, byte)
			dump_bel(self.buffer)
			print("Writing CSV file ...")
			log_bel(self.buffer)
			self.index = 0
			del self.buffer[:]
			return self.st_get_delimiter

	def st_idle(self):
		return self.st_idle

	def run(self, data_rx):
		self.data_rx = data_rx
		self.state = self.state()

