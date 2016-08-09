# -*- coding: utf-8 -*-
import logging

def init_log(LOG_ENABLE):
	# create logger
	log = logging.getLogger()
	log.setLevel(logging.DEBUG)
	log.disabled = LOG_ENABLE
	# create console handler and set level to debug
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)

	# create formatter
	formatter = logging.Formatter("%(asctime)s - [ %(levelname)-8s] : %(message)s", "%Y-%m-%d %H:%M:%S")

	# add formatter to ch
	ch.setFormatter(formatter)

	# add ch to logger
	log.addHandler(ch)
	return log 
