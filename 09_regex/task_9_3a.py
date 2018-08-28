# -*- coding: utf-8 -*-

'''
Задание 9.3a

Переделать функцию parse_cfg из задания 9.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.
'''

import re

from pprint import pprint

def parse_cfg(config):
	regex = ('interface (?P<interface>\S+\d)'
		 '|ip address (?P<ip>\S+\d (255)\.\d*\.\d*\.\d*)')
	result = {}
	with open(config) as data:
		match_iter = re.finditer(regex, data.read())
		for match in match_iter:
			if match.lastgroup == 'interface':
				interface = match.group(match.lastgroup)
				result[interface] = ()
			elif match.lastgroup == 'ip':
				result[interface] = tuple(match.group(match.lastgroup).split(' '))
	
	return result
					
out_print = parse_cfg('config_r1.txt')
pprint (out_print)
