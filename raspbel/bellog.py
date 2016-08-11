# -*- coding: utf-8 -*-

import csv
import logging
import os.path
from belbd import *
from belcsv import *
from bellogger import *
from belparser import *

def get_row(p):
	bel_list = [( p.get_num_pacs(), p.get_num_serie(), p.get_id_radio(), p.get_cod_equipamento(), p.get_id_cba(), \
		          p.get_personalidade(), p.get_versao_fw(), p.get_estado_cec(), p.get_estado_ciclo(), \
	              p.get_estado_maquina(), p.get_data_hora(), p.get_speed(), p.get_heading(), \
	              p.get_tamanho_implemento(), p.get_num_implementos(), p.get_latitude(), p.get_longitude()
	            )]
	return bel_list


def log_bel(frame):
	# Getting instance of log
	logger = Logger(Define.BELLOG_DEBUG_DISABLED)
	log = logger.get_instance()

	# Getting parser object
	p = Parser(frame)

	# Write frame to csv file
	log.debug("Receiving Bel package from radio: {}".format(p.get_id_radio()))
	write_to_file(get_row(p))

	# Save frame to DB
	save_to_db(get_row(p))
