# -*- coding: utf-8 -*-
'''
Задание 7.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt
'''

ignore = ['!', 'alias', 'Current configuration']
k = 0

def get_int_vlan_map(config):
	"""
        config - имя конфигурационного файла коммутатора

        Возвращает кортеж словарей:
        - первый словарь: порты в режиме access
        { 'FastEthernet0/12': 10,
        'FastEthernet0/14': 11,
        'FastEthernet0/16': 17  }
        - второй словарь: порты в режиме trunk
        { 'FastEthernet0/1':[10, 20],
        'FastEthernet0/2':[11, 30],
        'FastEthernet0/4':[17] }

        """
	ignore = ['switchport trunk allowed', 'switchport access vlan', 'Ethernet']
	k = 0
	result = []
	d_tr = {}
	d_ac = {}
	t_d = ()

	with open(config) as f:
		for line in f:
			for j in ignore:
				if j in line:
					result.append(line.rstrip())
		el = 0
		for j in result:
			el = el + 1
		n = 1
		while n < el:
			if result[n].startswith(' switchport trunk allowed'):
				d_tr[result[n-1]] = result[n].replace(" switchport trunk allowed vlan ", "").split(",")
			elif result[n].startswith(' switchport access vlan'):
				d_ac[result[n-1]] = int(str(result[n]).replace("switchport access vlan ", ""))
			n = n + 2
		t_d = (d_tr, d_ac)
		return t_d

t = get_int_vlan_map('config_sw1.txt')
print t






