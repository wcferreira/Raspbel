#!/usr/bin/python3

import sys
import time

x = 1
while True:
	try:
		print(x)
		time.sleep(.3)
		x += 1
	except KeyboardInterrupt:
		print('Bye')
		sys.exit()


