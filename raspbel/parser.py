# -*- coding: utf-8 -*-

import time
from datetime import datetime

class Parser:
	buffer = []

	def __init__(self, payload):
		Parser.buffer = payload

	def get_num_pacs(self):
		return str(int.from_bytes(Parser.buffer[15:16], byteorder='big'))

	def get_num_serie(self):
		return str(int.from_bytes(Parser.buffer[16:17], byteorder='big'))

	def get_id_radio(self):
		return str("{:X}".format(int.from_bytes(Parser.buffer[21:29], byteorder='big')))

	def get_cod_equipamento(self):
		str(int.from_bytes(Parser.buffer[29:35], byteorder='little'))

	def get_id_cba(self):
		return str("{:X}".format(int.from_bytes(Parser.buffer[35:41], byteorder='little')))

	def get_personalidade(self):
		return str(int.from_bytes(Parser.buffer[41:43], byteorder='little'))

	def get_versao_fw(self):
		return str(int.from_bytes(Parser.buffer[43:44], byteorder='little')) 

	def get_estado_cec(self):
		return str(int.from_bytes(Parser.buffer[44:45], byteorder='little'))

	def get_estado_ciclo(self):
		return str(int.from_bytes(Parser.buffer[45:46], byteorder='little'))

	def get_estado_maquina(self):
		return str(int.from_bytes(Parser.buffer[46:47], byteorder='little'))

	def get_data_hora(self):
		timestamp = int.from_bytes(Parser.buffer[47:51], byteorder='little')
		dt_obj = datetime.fromtimestamp(timestamp)
		return str(dt_obj.strftime("%d/%m/%y %H:%M"))

	def get_latitude(self):
		return str(int.from_bytes(Parser.buffer[51:59], byteorder='little'))

	def get_longitude(self):
		return str(int.from_bytes(Parser.buffer[59:67], byteorder='little'))

	def get_speed(self):
		return str(int.from_bytes(Parser.buffer[67:71], byteorder='little'))

	def get_heading(self):
		return str(int.from_bytes(Parser.buffer[87:91], byteorder='little'))

	def get_tamanho_implemento(self):
		return str(int.from_bytes(Parser.buffer[91:95], byteorder='little'))

	def get_num_implementos(self):
		return str(int.from_bytes(Parser.buffer[95:96], byteorder='little'))
