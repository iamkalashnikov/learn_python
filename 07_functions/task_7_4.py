# -*- coding: utf-8 -*-
'''
Задание 7.4

Создать функцию, которая обрабатывает конфигурационный файл коммутатора
и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

'''

ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
	
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
	
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    ignore_command = False
	
    for word in ignore:
        if word in command:
            return True
    return ignore_command

d_conf = []
result = []


def config_to_dict(config):
	"""
	config - имя конфигурационного файла

	Возвращает словарь:
	- Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
	- Если у команды верхнего уровня есть подкоманды,
	они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
	- Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
	"""
	with open(config) as f:
		n = 0
		for line in f:
			if ignore_command(line, ignore) == False and line.startswith(" ") == False and not line.startswith('!') and not line.startswith('\n'):
				d_conf.append(line.rstrip())
				n = n + 1
		result = [None] * n
		for i in range(n):
			result[i] = []
		k = 0
		f.seek(0)
		
		for l in f:
			if k > n:
				break
			elif ignore_command(l, ignore) == False and l.startswith(" ") == True and not l.startswith('!'):
				result[k].append(l.rstrip())
			elif ignore_command(l, ignore) == False and l.startswith(" ") == False and not l.startswith('!') and not l.startswith('\n'):
				result[k].append(None)
				k = k + 1
		result.append([None])
		result.pop(0)
	print d_conf
	print '\n' * 2
	print result
	print '\n' * 2
	dict_fin = dict(zip(d_conf, result))
	print dict_fin
	

config_to_dict('config_r1.txt')
