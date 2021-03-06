# -*- coding: utf-8 -*-

import re

'''
Задание 9.1

Создать скрипт, который будет ожидать два аргумента:
    1. имя файла, в котором находится вывод команды show
    2. регулярное выражение

В результате выполнения скрипта, на стандартный поток вывода должны быть
выведены те строки из файла с выводом команды show,
в которых было найдено совпадение с регулярным выражением.

Проверить работу скрипта на примере вывода команды sh ip int br (файл sh_ip_int_br.txt).
Например, попробуйте вывести информацию только по интерфейсу FastEthernet0/1.
'''

match = '0/1'
result = []
def check_regex(config, regex):
	with open(config) as f:
		for line in f:
			if re.findall(regex, line):
				result.append(line)
			else:
				pass
	return result

func = check_regex('sh_ip_int_br.txt', match)
print(func)
