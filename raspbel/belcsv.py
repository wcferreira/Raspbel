# -*- coding: utf-8 -*-

import csv
import os.path
from beldefine import Define
from bellogger import *

def write_to_file(frame):
	logger = Logger(Define.BELCSV_DEBUG_DISABLED)
	log = logger.get_instance()
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

		log.debug("Writing CSV file")
		f_bel.writerows(frame)
