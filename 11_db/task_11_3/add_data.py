# -*- coding: utf-8 -*-

"""
Задание 11.1

* add_data.py
 * с помощью этого скрипта, мы будем добавлять данные в БД
  * теперь у нас есть не только данные из вывода sh ip dhcp snooping binding,
    но и информация о коммутаторах

Соответственно, в файле add_data.py у нас будет две части:
* запись информации о коммутаторах в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* запись информации на основании вывода sh ip dhcp snooping binding
 * теперь у нас есть вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch,
   нам нужно его заполнять. Имя коммутатора мы определяем по имени файла с данными

"""

import glob
import yaml
import sqlite3
import re
from pprint import pprint

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
conn = sqlite3.connect(db_filename)

def create_data_list(dhcp_files):

	""" There is list h[] use for correctly name of switch when it adds to main list named result[] in current function. dhcp_files - just list of string names"""
	result = []
	regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
	regex_sw = re.compile('\S+\d+')
	for i in dhcp_files:
		name_sw = re.search(regex_sw, i).group()
		with open(i) as data:
			for line in data:
				match = regex.search(line)
				h = []
				if match:
					h = list(match.groups())
					h.append(name_sw)
					result.append(h)
				else:
					pass

	return result

def add_data_to_db(connection_to_db, data_list):
	with open('switches.yml') as f:
		switches_file = yaml.load(f)
	for row in switches_file['switches'].items():
		try:
			with connection_to_db:
				query = '''replace into switches (hostname, location) values (?, ?)'''
				connection_to_db.execute(query, row)
		except sqlite3.IntegrityError as e:
			print('Error occured: ', e)

	for row in data_list:
		try:
			with connection_to_db:
				current_sw = row[-1]
				sw_query_one = ('''update dhcp set active = 0 where switch=(?)''')
				connection_to_db.executemany(sw_query_one, current_sw)
				query = '''replace into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'''
				connection_to_db.execute(query, row)
				sw_query_two = ('''update dhcp set active = 1 where active is null or switch=(?)''')
				connection_to_db.executemany(sw_query_two, current_sw)
		except sqlite3.IntegrityError as e:
			print('Error occured: ', e)
	connection_to_db.close()
	return 0
#def set_active(database):
	
database_list = create_data_list(dhcp_snoop_files)
add_data_to_db(conn, database_list)
