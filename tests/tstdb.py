#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
# http://stackoverflow.com/questions/2092757/python-and-sqlite-insert-into-table
# Larger example
#rows = [('1', '0', 'CDCDC', '1111', '55', '33333', '1', '5', '0', '0','09/08/2016 17:06','0', '0', '0', '0', '-22,393', '-55,20')]

con = lite.connect('bel.db')

with con: 
	cur = con.cursor()    
#	cur.execute("INSERT INTO tbl_bel VALUES ('9', '1', '0', 'ABABABABABABABAB', '1111', '555555555555', '33333', '1', '5', '0', '0','09/08/2016 17:06','0', '0', '0', #'0', 		                                     '-22,3933669', '-55,204115')")   
	con.execute('''CREATE TABLE IF NOT EXISTS tbl_bel
			(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
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
			longitude TEXT NOT NULL);''')

	#cur.execute('INSERT INTO tbl_bel VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', rows)
	cur.execute("INSERT INTO tbl_bel VALUES ('1', '0', 'ABABABABABABABAB', '1111', '555555555555', '33333', '1', '5', '0',  '0','09/08/2016 17:06','0', '0', '0', '0','-22,3933669', '-55,204115')")   

