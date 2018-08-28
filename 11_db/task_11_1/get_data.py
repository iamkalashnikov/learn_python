# -*- coding: utf-8 -*-

'''
Это копия скрипта get_data_ver1.py из раздела
'''

import sqlite3
import sys

actual_args = ['mac', 'ip', 'vlan', 'interface', 'switch']
db_file = 'dhcp_snooping.db'

def check_args(db_filename):
	if len(sys.argv) == 1:
		with sqlite3.connect(db_filename) as conn:
			print('\nFull information')
			print ('-' * 74)
			query_script = "select * from dhcp;"
			result = conn.execute(query_script)
			print('mac                ip               vlan    interface           switch\n-----------------  --------------   ------  ---------------     ----------')		
			for el1,el2,el3,el4,el5 in result:
				print("{:<19}{:<17}{:<8}{:<20}{}".format(el1,el2,el3,el4,el5))

	elif len(sys.argv) == 3 and sys.argv[1] in actual_args:
		key, value = sys.argv[1:]
		keys = ['mac', 'ip', 'vlan', 'interface']
		keys.remove(key)
	
		with sqlite3.connect(db_filename) as conn:
	   		#Позволяет далее обращаться к данным в колонках, по имени колонки
			conn.row_factory = sqlite3.Row
			print ("\nDetailed information for host(s) with", key, value)
			print ('-' * 40)
			query = "select * from dhcp where {} = ?".format( key )
			result = conn.execute(query, (value,))
	
			for row in result:
				for k in keys:
					print ("{:12}: {}".format(k, row[k]))
				print ('-' * 40)
	elif len(sys.argv) > 3:
		print('Please, enter two or null arguments!')
	else:
		print('Entered parameter is not correct!\nPlease, enter again one of below: mac, ip, vlan, interface, switch')
	return 0

check_args(db_file)
