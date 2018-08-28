# -*- coding: utf-8 -*-

'''
Задание 10.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает аргумент output в котором находится вывод команды sh version
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

Функция write_to_csv:
* ожидает два аргумента:
 * имя файла, в который будет записана информация в формате CSV
 * данные в виде списка списков, где:
    * первый список - заголовки столбцов,
    * остальные списки - содержимое
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает

Остальное содержимое скрипта может быть в скрипте, а может быть в ещё одной функции.

Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print sh_version_files, чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''
from pprint import pprint
from tabulate import tabulate
import re
import glob
import csv

sh_version_files = glob.glob('sh_vers*')
print (sh_version_files)

headers = ['hostname     ', 'ios         ', 'uptime                ', 'image']
regex = ('(\d+\.\d+\(\d+\)\w+)' '|(\"(.+)\")' '|(\d+ days, .+ minutes)\s')
regex_for_names = ('r\d+')

result_vers = []
'''
for i in sh_version_files:
	match = re.search(regex_for_names, i)
	if match:
		result_vers.append(match.group()) 
print (result_vers)
'''
result_parse = []

def parse_sh_version(equip_name, output):
	with open(output) as data:
		result_parse = []
		count = 0
		for line in data:
			match = re.search(regex, line)
			if match and count == 0:
				result_parse.append('{:10}'.format(equip_name))
				result_parse.append('{:13}  '.format(match.group().rstrip().replace('"', '')))
				count = count + 1
			elif match and count >= 0:
				result_parse.append('{:13}  '.format(match.group().rstrip().replace('"', '')))		
	return tuple(result_parse)

l_to_f = [headers]

for u in sh_version_files:
	match = re.search(regex_for_names, u)
	if match:
		#l_to_f.append(match.group())
		l_to_f.append(parse_sh_version(match.group(), u))

def write_to_csv(wr_file, liist):
	with open(wr_file, 'w') as f:
		writer = csv.writer(f, escapechar = ' ', quoting=csv.QUOTE_NONE, delimiter = ' ')
		for row in liist:
			writer.writerow(row)

#pprint (parse_sh_version('sh_version_r1.txt'))
write_to_csv('routers_inventory.csv', l_to_f)


