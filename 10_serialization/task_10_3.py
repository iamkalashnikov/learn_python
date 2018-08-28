# -*- coding: utf-8 -*-

'''
Задание 10.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re
from pprint import pprint

def parse_sh_cdp_neighbors(output):
	with open(output) as f:
		line = f.read()
	match_device = re.finditer('(\S+)>', line)
	for match in match_device:
		name_device = match.group(1)
	list_columns = []
	fa = []
	int_dict = {}
	dev_dict = {}
	match_columns = re.finditer('(?P<device_id>[a-z|A-Z]+\d+) +'
								'(?P<local_int>\S+ \d+\/\d+) +'
								'(?P<hold_time>\d+) +'
								'(?P<capability>[A-Z] |[A-Z] [A-Z] |[A-Z] [A-Z] [A-Z] ) +'
								'(?P<platform>\d+|\w+-\w+-) +'
								'(?P<port_id>\S+ \d+\/\d+)', line)
	for match in match_columns:
		list_columns.append(match.groups())
	for device in list_columns:
		dev_dict.update({device[0] : device[5]})
		fa.append(device[1])

	int_dict = dict(zip(fa, dev_dict.items()))
	final_dict = {name_device : int_dict}	
	return final_dict

#pprint(parse_sh_cdp_neighbors('sh_cdp_n_sw1.txt'))

