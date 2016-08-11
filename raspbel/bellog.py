# -*- coding: utf-8 -*-

import csv
import logging
import os.path
from define import Define
from log import *
from parser import *

def get_row(p):
	
	bel_list = [( p.get_num_pacs(), p.get_num_serie(), p.get_id_radio(), p.get_cod_equipamento(), p.get_id_cba(), \
		          p.get_personalidade(), p.get_versao_fw(), p.get_estado_cec(), p.get_estado_ciclo(), \
	              p.get_estado_maquina(), p.get_data_hora(), p.get_speed(), p.get_heading(), \
	              p.get_tamanho_implemento(), p.get_num_implementos(), p.get_latitude(), p.get_longitude()
	            )]
	return bel_list

def log_bel(frame):
	logger = Logger(Define.PARSER_DEBUG_DISABLED)
	log = logger.get_instance()
	p = Parser(frame)
	file_exists = os.path.isfile('bel.csv')

	with open('bel.csv', 'a') as belfile:	
		headers = ['NumPacs', 'NumSerie', 'IDRadio', 'CodEquipamento', 'IDCBA', 
		           'Personalidade', 'VersaoFW', 'EstadoCEC', 'EstadoCiclo', 
		           'EstadoMaquina', 'DHPacote', 'Velocidade', 'Heading', 
		           'TamanhoImp', 'NumImo', 'Lat', 'Long'
		          ]

		f_bel = csv.writer(belfile)

		if not file_exists:
			f_bel.writerow(headers)

		log.debug("Receiving Bel package from radio: {}".format(p.get_id_radio()))
		f_bel.writerows(get_row(p))
