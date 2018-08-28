# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

    В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt
'''

def get_int(config):
        """
        config - имя конфигурационного файла коммутатора

        Возвращает кортеж словарей:
        - первый словарь: порты в режиме access
        { 'FastEthernet0/12':10,
        'FastEthernet0/14':11,
        'FastEthernet0/16':17 }
        - второй словарь: порты в режиме trunk
        { 'FastEthernet0/1':[10,20],
        'FastEthernet0/2':[11,30],
        'FastEthernet0/4':[17] }

        """
    	ignore = ['switchport trunk allowed', 'switchport access vlan', 'Ethernet']
	k = 0
	result = []
	d_tr = {}
	d_ac = {}

	with open(config) as f:
		for line in f:
			for j in ignore:
				if j in line:
					k = k + 1
			if not k < 1:
				result.append(line.rstrip())
			k = 0
		el = 0
		for j in result:
			el = el + 1
		n = 1
	
		while n < el:
			if result[n].startswith(' switchport trunk allowed'):
				d_tr[result[n-1]] = result[n].replace(" switchport trunk allowed vlan ", "").split(",")
				n = n + 2
			elif result[n].startswith(' switchport access vlan'):
				d_ac[result[n-1]] = int(str(result[n]).replace("switchport access vlan ", ""))
				n = n + 2
			elif result[n].startswith('interface'):
				d_ac[result[n-1]] = 1
				n = n + 1

		return d_tr, d_ac

t = get_int('config_sw2.txt')
print t