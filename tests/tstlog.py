#!/usr/bin/python3
# -*- coding: utf-8 -*-

from log import *

def bla():
	logger = Logger(False)
	log = logger.get_instance()
	log.debug('Barack Hussein Obama II')

if __name__ == "__main__":
	bla()
