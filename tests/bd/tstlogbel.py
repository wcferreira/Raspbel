#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
from bel import *

def get_num_pacs():
	return '8'

def get_num_serie():
	return '9'

def get_id_radio():
	return '00AABBCCDDEEFF88'

def get_cod_equipamento():
	return '1122'

def get_id_cba():
	return '000011225566'

def get_personalidade():
	return '32771'

def get_versao_fw():
	return '9'

def get_estado_cec():
	return '2'

def get_estado_ciclo():
	return '2'

def get_estado_maquina():
	return '2'

def get_dh_pacote():
	return '10/08/2016 23:54'

def get_velocidade():
	return '54'

def get_heading():
	return '1'

def get_tamanho_imp():
	return '22'

def get_num_imp():
	return '9'

def get_latitude():
	return '-22,12345'

def get_longitude():
	return '-44,12345'



singlepckg = [(get_num_pacs(), get_num_serie(), get_id_radio(), get_cod_equipamento(), get_id_cba(),
               get_personalidade(), get_versao_fw(), get_estado_cec(), get_estado_ciclo(), 
               get_estado_maquina(), get_dh_pacote(), get_velocidade(), get_heading(), 
               get_tamanho_imp(), get_num_imp(), get_latitude(), get_longitude())]

save_to_db(singlepckg)

