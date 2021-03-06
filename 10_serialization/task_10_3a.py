# -*- coding: utf-8 -*-

'''
Задание 10.3a

С помощью функции parse_sh_cdp_neighbors из задания 10.3,
обработать вывод команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}

Не копировать код функции parse_sh_cdp_neighbors
'''

import re
import re
import glob
import csv
import yaml
from tabulate import tabulate
from pprint import pprint
from task_10_3 import parse_sh_cdp_neighbors

sh_cdp_files = glob.glob('sh_cdp*')
rls = {}

for i in sh_cdp_files:
	rls.update(parse_sh_cdp_neighbors(i))
pprint(rls)

with open('topology.yaml',	'w') as	f:
	yaml.dump(rls, f)


