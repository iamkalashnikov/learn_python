# -*- coding: utf-8 -*-
'''
Задание 2

Создать функции:
- generate_access_config - генерирует конфигурацию для access-портов,
                           на основе словарей access и psecurity из файла sw_templates.yaml
- generate_trunk_config - генерирует конфигурацию для trunk-портов,
                           на основе словаря trunk из файла sw_templates.yaml
- generate_ospf_config - генерирует конфигурацию ospf, на основе словаря ospf из файла templates.yaml
- generate_mngmt_config - генерирует конфигурацию менеджмент настроек, на основе словаря mngmt из файла templates.yaml
- generate_alias_config - генерирует конфигурацию alias, на основе словаря alias из файла templates.yaml
- generate_switch_config - генерирует конфигурацию коммутатора, в зависимости от переданных параметров,
                           использует для этого остальные функции
'''
import yaml
from pprint import pprint


access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

def generate_access_config(access, psecurity=False):	
	temp_access = yaml.load(open('sw_templates.yaml'))
	result = []
	for intf, vlan in access.items():
		result.append('interface ' + intf)
		if psecurity == False:
			for command in temp_access['access']:
				if command.endswith('access vlan'):
					result.append(' {} {}'.format(command, vlan))
				else:
					result.append(' {}'.format(command))
		else:
			for command in temp_access['access']:
				if command.endswith('access vlan'):
					result.append(' {} {}'.format(command, vlan))
				else:
					result.append(' {}'.format(command))
			for command in temp_access['psecurity']:
				result.append(' {}'.format(command))
	return result


def generate_trunk_config(trunk):
	temp_trunk = yaml.load(open('sw_templates.yaml'))
	result = []
	for intf, vlan in trunk.items():
		result.append('interface ' + intf)
		for command in temp_trunk['trunk']:
			if command.endswith('allowed vlan'):
				for i in vlan:
					result.append(' {} {}'.format(command, i))
			else:
				result.append(' {}'.format(command))
	return result


def generate_ospf_config(filename):
   
	templates = yaml.load(open(filename))
	result = []
	result.append('OSPF information')
	for command in templates['ospf']:
		result.append(' {}'.format(command))
	return result


def generate_mngmt_config(filename):

	templates_mngmt = yaml.load(open(filename))
	result = []
	result.append('Management information')
	for command in templates_mngmt['mngmt']:
		result.append(' {}'.format(command))
	return result

def generate_alias_config(filename):

	templates_alias = yaml.load(open(filename))
	result = []
	result.append('Alias information')
	for command in templates_alias['alias']:
		result.append(' {}'.format(command))
	return result


def generate_switch_config(access=True, psecurity=False, trunk=True, ospf=True, mngmt=True, alias=False):
	result = []
	if access and psecurity:
		result.append(generate_access_config(access_dict, psecurity=True))
	else:
		pass
	if access and psecurity == False:
		result.append(generate_access_config(access_dict, psecurity=False))
	else:
		pass
	if trunk:
		result.append(generate_trunk_config(trunk_dict))
	else:
		pass
	if ospf:
		result.append(generate_ospf_config('templates.yaml'))
	else:
		pass
	if mngmt:
		result.append(generate_mngmt_config('templates.yaml'))
	else:
		pass
	if alias:
		result.append(generate_alias_config('templates.yaml'))
	else:
		pass
	return result

# Сгенерировать конфигурации для разных коммутаторов:

sw1 = generate_switch_config()
sw2 = generate_switch_config(psecurity=True, alias=True)
sw3 = generate_switch_config(ospf=False)

# Testing

for i in sw1:
	print ('\n'.join(i))
