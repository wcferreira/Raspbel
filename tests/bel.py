#!/usr/bin/python3

# -*- coding: utf-8 -*-
import csv
import os.path


rows = [   (1,      0,     0x0013A20040C893E5, 1003,   0x000016E26974, 32777, 1, 5, 0, 0, '28/07/2016 09:35', 1, 4, 7, 0, -22, 3933699, -55, ),
	       (1,      0,     0x0013A20040C893F6, 721036, 0x0000170126B8, 32769, 1, 1, 7, 6, '29/08/2016 10:46', 2, 5, 8, 1, -34, 6943789, -66, ),
	       (1,      0,     0x0013A20040C893F7, 721037, 0x0000170126B9, 32770, 2, 3, 4, 5, '30/09/2016 11:57', 3, 6, 9, 2, -36, 6953879, -76, ),]

file_exists = os.path.isfile('bel.csv')

with open('bel.csv', 'w') as f:	
	headers = ['NumPacs', 'NumSerie', 'IDRadio', 'CodEquipamento', 'IDCBA', 
               'Personalidade', 'VersaoFW', 'EstadoCEC', 'EstadoCiclo', 
               'EstadoMaquina', 'DHPacote', 'Velocidade', 'Heading', 
               'TamanhoImp', 'NumImo', 'Lat', 'Long', 'Col']

	f_foo = csv.writer(f)

	if not file_exists:
		f_foo.writerow(headers)

	f_foo.writerows(rows)
