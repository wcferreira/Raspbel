#!/usr/bin/python3

import signal
import sys

def handler(signum, frame):
	print('You pressed CTRL+C')
	sys.exit(0)

signal.signal(signal.SIGINT, handler)
print('Press CTRL+C')
signal.pause()
