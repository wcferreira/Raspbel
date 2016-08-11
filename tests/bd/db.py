#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

print('Sqlite3 + Python Test Drive')

# Creates or opens a file called tst with a SQLite3 DB
db = sqlite3.connect('tst.db')

# Get a cursor object
cursor = db.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                                name TEXT NOT NULL,
                                                phone TEXT NOT NULL,
                                                email TEXT NOT NULL,
                                                password TEXT NOT NULL)
               ''')
db.commit()

name1 = 'Barack Hussein Obama'
phone1 = '3366858'
email1 = 'barack.obama@whitehouse.gov.us'
password1 = 'b4r4ck.0b4m4'

name2 = 'Michelle Obama'
phone2 = '5557241'
email2 = 'michelle.obama@whitehouse.gov.us'
password2 = 'm1ch3ll3.0b4m4'

# Insert user 1
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES (?, ?, ?, ?)''', (name1, phone1, email1, password1))

# Insert user 2
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES (?, ?, ?, ?)''', (name2, phone2, email2, password2))

cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES (:name, :phone, :email, :password)''',
                  {'name':'Maria Terezinha',
                   'phone':'982962036',
                   'email':'maria.carvalho@gmail.com',
                   'password':'m4r14.c4rv4lh0'})

users = [('Sergio Yamada', '21871800', 'sergio.yamada@auteq.com.br', 's3g101'),
         ('Roberto Borges', '21871800', 'roberto.borges@auteq.com.br', 'r0b3rt0'),
         ('Joao Rocha', '21871800', 'joao.rocha@auteq.com.br', 'j040'),
         ('Paulo Melo', '21871800', 'paulo.melo@auteq.com.br', 'p4ul0')]

cursor.executemany('''INSERT INTO users (name, phone, email, password) 
                      VALUES (?, ?, ?, ?)''', users)


def getName():
	return 'Wagner Ferreira'

def getPhone():
	return '21871800'

def getEmail():
	return 'wagner.ferreira@auteq.com.br'

def getPassword():
	return 'w4gn3r'

myuser = [(getName(), getPhone(), getEmail(), getPassword())]

cursor.executemany('''INSERT INTO users(name, phone, email, password)
                      VALUES (?, ?, ?, ?)''', myuser)
db.commit()

db.close()


