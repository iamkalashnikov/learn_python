# -*- coding: utf-8 -*-
import re
'''
Задание 9.1c

Проверить работу скрипта из задания 9.1 и регулярного выражения из задания 9.1a или 9.1b
на выводе sh ip int br из файла sh_ip_int_br_switch.txt.

Если, в результате выполнения скрипта, были выведены не только строки
с интерфейсами 0/1 и 0/3, исправить регулярное выражение.
В результате, должны выводиться только строки с интерфейсами 0/1 и 0/3.
'''
match = '0/1 |0/3 '
result = []
def check_regex(config, regex):
	with open(config) as f:
		for line in f:
			if re.findall(regex, line):
				result.append(line)
			else:
				pass
	return result

func = check_regex('sh_ip_int_br_switch.txt', match)
for el in func:
	print (el)