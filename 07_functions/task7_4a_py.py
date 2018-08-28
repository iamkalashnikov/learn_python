# -*- coding: utf-8 -*-
from collections import OrderedDict
ignore = ['duplex', 'alias', 'Current configuration']


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


def config_to_dict(config):
    """
    config - имя конфигурационного файла
    """

    result = OrderedDict()
    current_section = ''
    section_children = []

    with open(config) as f:
        for line in f:
            line = line.rstrip()

            if not line or line.startswith('!') or line[1]=='!' or check_ignore(line, ignore):
                pass

            elif line[0].isalnum():
                if current_section:
                    result[ current_section ] = section_children
                    section_children = []
                current_section = line

            elif line.startswith(' ') and line[1].isalnum():
                last_child = line
                section_children.append( line )

            else:
                if type(section_children) is list:
                    section_children = OrderedDict({ key: [] for key in section_children })

                section_children[ last_child ].append(line)

    return result

result_dict = config_to_dict('config_r1.txt')

for key in result_dict:
    print key
    print result_dict[key]