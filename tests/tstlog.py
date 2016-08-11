#!/usr/bin/python3
# -*- coding: utf-8 -*-

from log import *

def bla():
	logger = Logger(False)
	log = logger.get_instance()
	log.debug('Barack Hussein Obama II')
	log.info('Barack Hussein Obama II')
	log.warn('Barack Hussein Obama II')
	log.error('Barack Hussein Obama II')

if __name__ == "__main__":
	bla()
