# -*- coding: utf-8 -*-

from collections import OrderedDict
from draw_network_graph import *
import task_8_2

"""
Задание 8.2b

С помощью функции parse_cdp_neighbors из задания 8.2
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_8_2b_topology.svg

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""


def dict_add_keep_last(a, b): # aka merged() or updated()
    d = a.copy()
    d.update(b)
    return d


conf_dict1 = task_8_2.parse_cdp_neighbours('sh_cdp_n_r1.txt')
conf_dict2 = task_8_2.parse_cdp_neighbours('sh_cdp_n_r2.txt')
conf_dict3 = task_8_2.parse_cdp_neighbours('sh_cdp_n_r3.txt')
conf_dict4 = task_8_2.parse_cdp_neighbours('sh_cdp_n_sw1.txt')

cdf1 = dict_add_keep_last(conf_dict1, conf_dict2)
cdf2 = dict_add_keep_last(cdf1, conf_dict3)
cdf3 = dict_add_keep_last(cdf2, conf_dict4)

print cdf3

draw_topology(cdf3)
