# -*- coding: utf-8 -*-

from draw_network_graph import *
from task_8_2 import *

conf_dict = parse_cdp_neighbours('sw1_sh_cdp_neighbors.txt')

draw_topology(conf_dict)

