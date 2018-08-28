# -*- coding: utf-8 -*-

'''
Задание 9.3b

Проверить работу функции parse_cfg из задания 9.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 9.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.
'''
import re

from collections import OrderedDict
from pprint import pprint

def parse_cfg(config):
	regex = ('interface (?P<interface>\S+\d)'
		 '|ip address (?P<ip>\S+\d (255)\.\d*\.\d*\.\d*)')
	result = OrderedDict()
	current_section = ''
	section_children = []
	with open(config) as data:
		match_iter = re.finditer(regex, data.read())
		for match in match_iter:


			if match.lastgroup == 'interface':
				if current_section:
					result[ current_section ] = section_children
					section_children = []
				current_section = match.group(match.lastgroup)
	
			elif match.lastgroup == 'ip':
				last_child = tuple(match.group(match.lastgroup).split(' '))
				section_children.append( tuple(match.group(match.lastgroup).split(' ')) )
	
			else:
				if type(section_children) is list:
					section_children = OrderedDict({ key: [] for key in section_children })
	
				section_children[ last_child ].append(tuple(match.group(match.lastgroup).split(' ')))
	return result					
out_print = parse_cfg('config_r2.txt')
pprint (out_print)
