#-*- coding: utf-8 -*-

def generate_access_config(access):
	"""
	access - словарь access-портов,
	для которых необходимо сгенерировать конфигурацию, вида:
		{ 'FastEthernet0/12':10,
		'FastEthernet0/14':11,
		'FastEthernet0/16':17}
	Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
	"""	
	
	result = []

	access_template = [' switchport mode access',
		' switchport access vlan',
		' switchport nonegotiate',
		' spanning-tree portfast',
		' spanning-tree bpduguard enable']
	n = 0	

	for key in access:
		result.append(key)
		for k in access_template:
			if k.endswith('vlan'):
				result.append('{} {}'.format(k, access[key]))
			else:
				result.append(k)
	return result

def generate_trunk_config(trunk):
	"""
	trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.
	Возвращает список всех команд, которые были сгенерированы на основе шаблона
	"""
	trunk_template = [' switchport trunk encapsulation dot1q',
			' switchport mode trunk',
			' switchport trunk native vlan 999',
			' switchport trunk allowed vlan']
	result = []

	for key in trunk:
		result.append(key)
		for i in trunk_template:
			if i.endswith('vlan'):
				result.append('{} {}'.format(i, str(trunk[key])).replace("[", "").replace("]", ""))
			else:
				result.append(i)
	return result

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

