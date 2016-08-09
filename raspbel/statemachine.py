#!/usr/bin/python3

# -*- coding: utf-8 -*-
import logging
import sys
import time
from define import Define
from dump import *
from logbel import *

class StateMachine:

	def init_log(self):
		# create logger
		self.log = logging.getLogger(__name__)
		self.log.setLevel(logging.DEBUG)
		self.log.disabled = Define.FSM_DEBUG_DISABLED
		# create console handler and set level to debug
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)

		# create formatter
		formatter = logging.Formatter("%(asctime)s - [ %(levelname)-8s] : %(message)s", "%Y-%m-%d %H:%M:%S")

		# add formatter to ch
		ch.setFormatter(formatter)

		# add ch to logger
		self.log.addHandler(ch)

	def init_fsm(self):
		self.buffer = []
		self.index = 0
		self.data_rx = 0
		self.length = 0
		self.cnt = 0
		self.is_escape_char = False
		
	def __init__(self):
		self.init_fsm()
		self.init_log()
		self.state = self.st_get_delimiter

	def st_get_delimiter(self):
		self.log.debug("State: Delimiter")
		if self.data_rx == Define.DELIMITER:
			self.buffer.insert(self.index, self.data_rx)
			self.index += 1
			return self.st_get_length_lsb
		else:
			return self.st_get_delimiter

	def st_get_length_lsb(self):
		self.log.debug("State: Length LSB")

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
			#self.log.debug("Length LSB: {:02x}".format(byte))
			self.index += 1
			return self.st_get_length_msb

	def st_get_length_msb(self):
		self.log.debug("State: Length MSB")

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
			#self.log.debug("Length MSB: {:02x}".format(byte))
			self.buffer.insert(self.index, byte)
			self.length = int.from_bytes(self.buffer[1:3], byteorder='big') - 1 # Get rid of Checksum (1byte)
			#self.log.debug("Length Parser: {}".format(self.length))
			self.log.debug(self.buffer)
			self.index += 1
			return self.st_get_data

	def st_get_data(self):
		byte = self.data_rx

		#self.log.debug("Escape: {}".format(self.is_escape_char))
		#self.log.debug("@@@ Length @@@: {}".format(self.length))

		if  self.cnt < self.length:
			self.log.debug("Count: {}".format(self.cnt))
			self.log.debug("State: Frame ID")

			if self.data_rx == Define.ESCAPE:
				self.log.debug("I've got a escape character")
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
		self.log.debug("State: Checksum")

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
			self.log.debug("Writing CSV file ...")
			log_bel(self.buffer)
			self.init_fsm()
			del self.buffer[:]
			return self.st_get_delimiter

	def run(self, data_rx):
		self.data_rx = data_rx
		self.state = self.state()
