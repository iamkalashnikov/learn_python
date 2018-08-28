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
	result_fin = []

	access_template = ['switchport mode access',
		'switchport access vlan',
		'switchport nonegotiate',
		'spanning-tree portfast',
		'spanning-tree bpduguard enable']
	n = 0	

	for key in access:
		result.append(key)
		for k in access_template:
			if k.endswith('vlan'):
				result.append('{} {}'.format(k, access[key]))
			else:
				result.append(k)
		#result_fin.append(' '.join(result))
	print result

access_dict = { 'FastEthernet0/12':10,
		'FastEthernet0/14':11,
		'FastEthernet0/16':17,
		'FastEthernet0/17':150 }
generate_access_config(access_dict)
