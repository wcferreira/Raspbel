# -*- coding: utf-8 -*-

import time
from datetime import datetime

def dump_bel(buffer):
	print("Payload Length:         {}".format(int.from_bytes(buffer[1:3], byteorder='big')))
	print("Frame ID:               {:02X}".format(int.from_bytes(buffer[3:4], byteorder='big')))
	print("64 bit Source Address:  {:X}".format(int.from_bytes(buffer[4:12], byteorder='big')))
	print("16 bit Source Address:  {:04X}".format(int.from_bytes(buffer[12:14], byteorder='big')))
	print("Receive Options:        {:02X}".format(int.from_bytes(buffer[14:15], byteorder='big')))
	print("Frame Sequence:         {:02X}".format(int.from_bytes(buffer[15:16], byteorder='big')))
	print("Number of Frames:       {:02X}".format(int.from_bytes(buffer[16:17], byteorder='big')))
	print("Frame Type:             {:04X}".format(int.from_bytes(buffer[17:19], byteorder='big')))
	print("Frame ID:               {:04X}".format(int.from_bytes(buffer[19:21], byteorder='big')))
	print("64 bit Source Address:  {:X}".format(int.from_bytes(buffer[21:29], byteorder='big')))
	print("Vehicle ID:             {:X}".format(int.from_bytes(buffer[29:35], byteorder='little')))
	print("Onboard Computer ID:    {:X}".format(int.from_bytes(buffer[35:41], byteorder='little')))
	print("Application ID:         {:04X}".format(int.from_bytes(buffer[41:43], byteorder='little')))
	print("M2M Firmware Version:   {:02X}".format(int.from_bytes(buffer[43:44], byteorder='little')))
	print("CEC State:              {:02X}".format(int.from_bytes(buffer[44:45], byteorder='little')))
	print("Status Automated Cycle: {:02X}".format(int.from_bytes(buffer[45:46], byteorder='little')))
	print("Machine Status:         {:02X}".format(int.from_bytes(buffer[46:47], byteorder='little')))
	
	timestamp = int.from_bytes(buffer[47:51], byteorder='little')
	dt_obj = datetime.fromtimestamp(timestamp)
	print("Date/Time:              {}".format(dt_obj.strftime("%d/%m/%y %H:%M")))
	print("Latitude:               {:X}".format(int.from_bytes(buffer[51:59], byteorder='little')))
	print("Longitude:              {:X}".format(int.from_bytes(buffer[59:67], byteorder='little')))
	print("Speed:                  {:X}".format(int.from_bytes(buffer[67:71], byteorder='little')))
	print("Latitude (Ref):         {:X}".format(int.from_bytes(buffer[71:79], byteorder='little')))
	print("Longitude (Ref):        {:X}".format(int.from_bytes(buffer[79:87], byteorder='little')))
	print("Heading:                {:4X}".format(int.from_bytes(buffer[87:91], byteorder='little')))
	print("Vehicle Length:         {:4X}".format(int.from_bytes(buffer[91:95], byteorder='little')))
	print("Number of ##:           {:2X}".format(int.from_bytes(buffer[95:96], byteorder='little')))
	
