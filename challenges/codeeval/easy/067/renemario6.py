# -*- coding: utf-8 -*-
import sys

archivo = open(sys.argv[1], 'r')

for i in archivo:
	line = i.strip()
	if line:
		print int(line,16)
archivo.close()
