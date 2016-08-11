#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

print('Sqlite3 + Python Test Drive')

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

belpckg = [('1', '0', '0013A20040C893E5', '1003', '000016E26974', '32777', '1', '5', 
            '0', '0', '29/07/2016 09:35', '0', '0', '0', '0', '-22,3933669', '-55,204115'),

           ('4', '0', '0013A20040C893F6', '721036', '0000170126B8', '32769', '1', '1', 
            '7', '6', '29/07/2016 09:35', '0', '48528696', '15200', '1', '-22,393839', '-55,203871'),

           ('1', '0', '0013A20040C892F7', '721035', '000016E26557', '32769', '1', '1', 
            '0', '6', '29/07/2016 09:35', '4', '7', '10616569', '15200', '-22,3986261', '-55,2045559')
          ]

cursor.executemany('''INSERT INTO tbl_bel (num_pacs, num_serie, id_radio, cod_equipamento,
                                           id_cba, personalidade, versao_fw, estado_cec, 
                                           estado_ciclo, estado_maquina, dh_pacote, velocidade, 
                                           heading, tamanho_imp, num_imp, latitude, longitude)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', belpckg)



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

cursor.executemany('''INSERT INTO tbl_bel (num_pacs, num_serie, id_radio, cod_equipamento,
                                           id_cba, personalidade, versao_fw, estado_cec, 
                                           estado_ciclo, estado_maquina, dh_pacote, velocidade, 
                                           heading, tamanho_imp, num_imp, latitude, longitude)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', singlepckg)
db.commit()

db.close()


