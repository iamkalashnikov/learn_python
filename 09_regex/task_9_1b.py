# -*- coding: utf-8 -*-

import re

'''
Задание 9.1b

Переделайте регулярное выражение из задания 9.1a таким образом, чтобы оно, по-прежнему,
отображало строки с интерфейсами 0/1 и 0/3, но, при этом, в регулярном выражении было не более 7 символов (не считая кавычки вокруг регулярного выражения).

Проверьте регулярное выражение, используя скрипт, который был создан в задании 9.1,
и файл sh_ip_int_br.txt.
'''

match = '0/1|0/3'
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
for el in func:
	print el