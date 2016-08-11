#!/usr/bin/python

# -*- coding: UTF-8 -*-


def getDoubleWord(buf):
  data = buf[3]
  data <<= 8
  data |= buf[2]
  data <<= 8
  data |= buf[1]
  data <<= 8
  data |= buf[0]
  return data

def getWord(buf):
  data = buf[1]
  data <<= 8
  data |= buf[0]
  return data

def getByte(buf):
	return buf[0]

def dumpSetOfBytes(data):
	lst_bytes = []
	for byte in data:
		lst_bytes.append(hex(byte))
	return lst_bytes

"""
def dumpVersaoCod():
	# UOS_sVersaoCod
	print('Flag Inicio:                       {:04x}'.format(getWord(registroOperacional[0:2])))

	if getWord(registroOperacional[2:4]) in modelo:
		print('Modelo:                            {}'.format(modelo[getWord(registroOperacional[2:4])]))
	else:
		print('Modelo:                            {}'.format(getWord(registroOperacional[2:4])))

	if getWord(registroOperacional[4:6]) in versao:
		print('Versao:                            {}'.format(versao[getWord(registroOperacional[4:6])]))
	else:
		print('Versao:                            {}'.format(getWord(registroOperacional[4:6])))

	print('Revisao:                           {:04x}'.format(getWord(registroOperacional[6:8])))
	print('Edicao:                            {:04x}'.format(getWord(registroOperacional[8:10])))
	print('Numero de Serie:                   {}'.format(dumpSetOfBytes(registroOperacional[10:16])))
	print('Tipo Arquivo:                      {:04x}'.format(getWord(registroOperacional[16:18])))
	print('Versao Arquivo:                    {:02x}'.format(getByte(registroOperacional[18:19])))
	print('Tipo CAN:                          {}'.format(tipoCAN[getByte(registroOperacional[19:20])]))
	print('Opcionais:                         {}'.format(dumpSetOfBytes(registroOperacional[20:28])))
	print('Offset dos Registros Operacionais: {:08x}'.format(getDoubleWord(registroOperacional[28:32])))
	print('')

def dumpCabecalhoP1():
	print('Id Equipamento:                    {:08x}'.format(getDoubleWord(registroOperacional[32:36])))
	print('Codigo de Frota:                   {}'.format(dumpSetOfBytes(registroOperacional[36:42])))
	print('Id Perfil Equipamento:             {:08x}'.format(getDoubleWord(registroOperacional[42:46])))
	print('Id Modelo:                         {:08x}'.format(getDoubleWord(registroOperacional[46:50])))
	print('Id Configuracao Operacional:       {:08x}'.format(getDoubleWord(registroOperacional[50:54])))
	print('Id Entrada Pulsada 1:              {:08x}'.format(getDoubleWord(registroOperacional[54:58])))
	print('Id Entrada Pulsada 2:              {:08x}'.format(getDoubleWord(registroOperacional[58:62])))
	print('Id Entrada Analogica 1:            {:08x}'.format(getDoubleWord(registroOperacional[62:66])))
	print('Id Entrada Analogica 2:            {:08x}'.format(getDoubleWord(registroOperacional[66:70])))
	print('Id Entrada Analogica 3:            {:08x}'.format(getDoubleWord(registroOperacional[70:74])))
	print('Id Entrada Analogica 4:            {:08x}'.format(getDoubleWord(registroOperacional[74:78])))
	print('Id Entrada Digital 1:              {:08x}'.format(getDoubleWord(registroOperacional[78:82])))
	print('Id Entrada Digital 2:              {:08x}'.format(getDoubleWord(registroOperacional[82:86])))
	print('Id Entrada Digital 3:              {:08x}'.format(getDoubleWord(registroOperacional[86:90])))
	print('Id Entrada Digital 4:              {:08x}'.format(getDoubleWord(registroOperacional[90:94])))
	print('Id Entrada Digital 5:              {:08x}'.format(getDoubleWord(registroOperacional[94:98])))
	print('Id Entrada Digital 6:              {:08x}'.format(getDoubleWord(registroOperacional[98:102])))
	print('Id Entrada Digital 7:              {:08x}'.format(getDoubleWord(registroOperacional[102:106])))
	print('Id Entrada Digital 8:              {:08x}'.format(getDoubleWord(registroOperacional[106:110])))
	print('Id Supervisor:                     {:08x}'.format(getDoubleWord(registroOperacional[110:114])))
	print('')


"""
if __name__ == "__main__":
	b = [0xb2, 0x6b, 0xa4, 0x57]
	#print('Data/Hora: {:08x}'.format(getDoubleWord(b[0:4])))
