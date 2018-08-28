#-*- coding: utf-8 -*-

def generate_trunk_config(trunk):
	"""
	trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.
	Возвращает список всех команд, которые были сгенерированы на основе шаблона
	"""
	trunk_template = ['switchport trunk encapsulation dot1q',
			'switchport mode trunk',
			'switchport trunk native vlan 999',
			'switchport trunk allowed vlan']
	result = []

	for key in trunk:
		result.append(key)
		for i in trunk_template:
			if i.endswith('vlan'):
				result.append('{} {}'.format(i, str(trunk[key])).replace("[", "").replace("]", 							""))
			else:
				result.append(i)
	print result

trunk_dict = { 'FastEthernet0/1':[10,20,30],
		'FastEthernet0/2':[11,30],
		'FastEthernet0/4':[17] }
	
generate_trunk_config(trunk_dict)
