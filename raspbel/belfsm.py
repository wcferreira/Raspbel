#!/usr/bin/python3

# -*- coding: utf-8 -*-
import logging
import sys
import time
from define import Define
from dump import *
from log import init_log
from logbel import *

class StateMachine:
	def init_fsm(self):
		self.buffer = []
		self.index = 0
		self.data_rx = 0
		self.length = 0
		self.cnt = 0
		self.is_escape_char = False
		
	def __init__(self):
		self.logger = Logger(Define.FSM_DEBUG_DISABLED)
		self.log = self.logger.get_instance()
		self.init_fsm()
		self.state = self.st_get_delimiter

	def st_get_delimiter(self):
		#self.log.debug("State: Delimiter")
		if self.data_rx == Define.DELIMITER:
			self.buffer.insert(self.index, self.data_rx)
			self.index += 1
			return self.st_get_length_lsb
		else:
			return self.st_get_delimiter

	def st_get_length_lsb(self):
		#elf.log.debug("State: Length LSB")

		byte = self.data_rx
		if byte == Define.ESCAPE:
			#self.log.debug("I've got a escape character")
			self.is_escape_char = True
			return self.st_get_length_lsb
		else:
			if self.is_escape_char == True:
				#self.log.debug("Treating escape character")
				self.is_escape_char = False
				byte = self.data_rx ^ 0x20

		if self.is_escape_char == False:
			self.buffer.insert(self.index, byte)
			self.index += 1
			return self.st_get_length_msb

	def st_get_length_msb(self):
		#self.log.debug("State: Length MSB")

		byte = self.data_rx
		if byte == Define.ESCAPE:
			#self.log.debug("I've got a escape character")
			self.is_escape_char = True
			return self.st_get_length_msb
		else:
			if self.is_escape_char == True:
				#self.log.debug("Treating escape character")
				self.is_escape_char = False
				byte = self.data_rx ^ 0x20

		if self.is_escape_char == False:
			self.buffer.insert(self.index, byte)
			self.length = int.from_bytes(self.buffer[1:3], byteorder='big') - 1 # Get rid of Checksum (1byte)
			self.index += 1
			return self.st_get_data

	def st_get_data(self):
		byte = self.data_rx

		if  self.cnt < self.length:
			if self.data_rx == Define.ESCAPE:
				#self.log.debug("I've got a escape character")
				self.is_escape_char = True
			else:
				if self.is_escape_char == True:
					#self.log.debug("Treating escape character")
					self.is_escape_char = False
					byte = self.data_rx ^ 0x20

			if self.is_escape_char == False:
				self.buffer.insert(self.index, byte)
				self.cnt += 1
				self.index += 1

			return self.st_get_data
		else:
			return self.get_checksum

	def get_checksum(self):
		#self.log.debug("State: Checksum")

		byte = self.data_rx
		if byte == Define.ESCAPE:
			#self.log.debug("I've got a escape character")
			self.is_escape_char = True
			return self.get_checksum
		else:
			if self.is_escape_char == True:
				#self.log.debug("Treating escape character")
				self.is_escape_char = False
				byte = self.data_rx ^ 0x20

		if self.is_escape_char == False:
			self.buffer.insert(self.index, byte)
			#self.log.debug("Writing CSV file ...")
			log_bel(self.buffer)
			self.init_fsm()
			del self.buffer[:]
			return self.st_get_delimiter

	def run(self, data_rx):
		self.data_rx = data_rx
		self.state = self.state()

