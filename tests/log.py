# -*- coding: utf-8 -*-
import logging

class Logger:
	def __init__(self, onoff):
		self.onoff = onoff

	def get_instance(self):
		# create logger
		log = logging.getLogger()
		log.setLevel(logging.DEBUG)
		log.disabled = self.onoff
		# create console handler and set level to debug
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)

		# create formatter
		formatter = logging.Formatter("%(asctime)-8s %(filename)-8s %(funcName)8s() %(lineno)s [ %(levelname)-8s ]: %(message)s", 
                                      "%Y-%m-%d %H:%M:%S")

		# add formatter to ch
		ch.setFormatter(formatter)

		# add ch to logger
		log.addHandler(ch)
		return log 