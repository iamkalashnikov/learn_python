# -*- coding: utf-8 -*-

"""
Задание 8.2

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

"""
ignore = ['Device', 'Capability', ',', 'show']
def check_ignore(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    """
    ignore_command = False

    for word in ignore:
        if word in command:
            ignore_command = True
    return ignore_command

def parse_cdp_neighbours(config):
	result = []
	keys = []
	valuez = []
	with open(config) as f:
		n = 0
		k = 0
		for line in f:
			if '>' in line:
				index = line.find('>')
				name_device = line[0:index]
			elif check_ignore(line, ignore) or line.startswith("\n"):
				pass
			else:
				result.append(line.split())
				k = k + 1

		for v in result:
			for i in v:
				if i == 'S' or i == 'R' or i == 'I' and n < k:
					result[n].remove("{}".format(i))
				elif i == result[n][-1]:
					n = n + 1
					break
				
		for i in result:
				keys.append(tuple(('{},{}{}'.format(name_device, i[1], i[2])).split(',')))
				valuez.append(tuple(('{},{}{}'.format(i[0], i[6], i[7])).split(',')))
		fin_dict = dict(zip(keys, valuez))

		return fin_dict
"""
final = parse_cdp_neighbours('sw1_sh_cdp_neighbors.txt')
print final
"""