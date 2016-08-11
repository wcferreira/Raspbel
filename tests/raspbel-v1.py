#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

def save_to_db(belpckg):
	print('Saving bel package into DB')
	# Creates or opens a file called tst with a SQLite3 DB
	db = sqlite3.connect('bel.db')

	# Get a cursor object
	cursor = db.cursor()
	cursor.execute('''
		           CREATE TABLE IF NOT EXISTS tbl_bel (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		                                               num_pacs TEXT NOT NULL,
		                                               num_serie TEXT NOT NULL,
		                                               id_radio TEXT NOT NULL,
		                                               cod_equipamento TEXT NOT NULL,
		                                               id_cba TEXT NOT NULL,
		                                               personalidade TEXT NOT NULL,
		                                               versao_fw TEXT NOT NULL,
		                                               estado_cec TEXT NOT NULL,
		                                               estado_ciclo TEXT NOT NULL,
		                                               estado_maquina TEXT NOT NULL,
		                                               dh_pacote TEXT NOT NULL,
		                                               velocidade TEXT NOT NULL,
		                                               heading TEXT NOT NULL,
		                                               tamanho_imp TEXT NOT NULL,
		                                               num_imp TEXT NOT NULL,
		                                               latitude TEXT NOT NULL,
		                                               longitude TEXT NOT NULL)               
		           ''')



	cursor.executemany('''INSERT INTO tbl_bel (num_pacs, num_serie, id_radio, cod_equipamento,
		                                       id_cba, personalidade, versao_fw, estado_cec, 
		                                       estado_ciclo, estado_maquina, dh_pacote, velocidade, 
		                                       heading, tamanho_imp, num_imp, latitude, longitude)
		                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', belpckg)
	db.commit()

	db.close()


