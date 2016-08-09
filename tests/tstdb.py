#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
# http://stackoverflow.com/questions/2092757/python-and-sqlite-insert-into-table
# Larger example
rows = [(3,'1', '0', 'CDCDC', '1111', '55', '33333', '1', '5', '0', '0','09/08/2016 17:06','0', '0', '0', '0', '-22,393', '-55,20')]

con = lite.connect('bel.db')

with con: 
	cur = con.cursor()    
#	cur.execute("INSERT INTO tbl_bel VALUES ('9', '1', '0', 'ABABABABABABABAB', '1111', '555555555555', '33333', '1', '5', '0', '0','09/08/2016 17:06','0', '0', '0', #'0', 		                                     '-22,3933669', '-55,204115')")
	cur.execute('INSERT INTO tbl_bel VALUES (?,?,?,?,?)', rows)
	con.commit()



