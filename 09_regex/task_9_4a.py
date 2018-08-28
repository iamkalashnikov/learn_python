# -*- coding: utf-8 -*-

'''
Задание 9.4a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей с результатами отработки функции parse_sh_ip_int_br из задания 9.4

Функция возвращает результат в виде списка словарей (порядок полей может быть другой):
[{'interface': 'FastEthernet0/0', 'status': 'up', 'protocol': 'up', 'address': '10.0.1.1'},
 {'interface': 'FastEthernet0/1', 'status': 'up', 'protocol': 'up', 'address': '10.0.2.1'}]

Проверить работу функции на примере файла sh_ip_int_br_2.txt:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функции parse_show из прошлого задания.

Функцию parse_sh_ip_int_br не нужно копировать.
Надо импортировать или саму функцию, и использовать то же регулярное выражение,
что и в задании 9.4, или импортировать результат выполнения функции parse_show.

'''

import re
from pprint import pprint
from task_9_4 import parse_ip_int_br

past_result = parse_ip_int_br('sh_ip_int_br_2.txt')

headers = ['interface', 'address', 'status', 'protocol']

result = []

def convert_to_dict(fields, out_tuples):
	for i in out_tuples:
		result.append(dict(zip(fields, i)))
	return result
t = convert_to_dict(headers, past_result)
pprint (t)
