#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
from beldefine import Define
from bellogger import *

def save_to_db(belpckg):
	logger = Logger(Define.BELBD_DEBUG_DISABLED)
	log = logger.get_instance()
	log.debug("Saving bel package in the DB")
	
	# Creates or opens a file called tst with a SQLite3 DB
	db = sqlite3.connect('bel.db')

	# Get a cursor object
	cursor = db.cursor()
	cursor.execute('''
		           CREATE TABLE IF NOT EXISTS tbl_bel (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                                       num_pacs TEXT,
                                                       num_serie TEXT,
                                                       id_radio TEXT,
                                                       cod_equipamento TEXT,
                                                       id_cba TEXT,
                                                       personalidade TEXT,
                                                       versao_fw TEXT,
                                                       estado_cec TEXT,
                                                       estado_ciclo TEXT,
                                                       estado_maquina TEXT,
                                                       dh_pacote TEXT,
                                                       velocidade TEXT,
                                                       heading TEXT,
                                                       tamanho_imp TEXT,
                                                       num_imp TEXT,
                                                       latitude TEXT,
                                                       longitude TEXT)
                  ''')

	cursor.executemany('''INSERT INTO tbl_bel (num_pacs, num_serie, id_radio, cod_equipamento,
		                                       id_cba, personalidade, versao_fw, estado_cec, 
		                                       estado_ciclo, estado_maquina, dh_pacote, velocidade, 
		                                       heading, tamanho_imp, num_imp, latitude, longitude)
		                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', belpckg)
	db.commit()

	db.close()
