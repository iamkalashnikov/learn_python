#-*- coding: utf-8 -*-

import my_func

from sys import argv

t_dict = my_func.get_int_vlan_map(argv[1])

a_c = my_func.generate_access_config(t_dict[0])

t_c = my_func.generate_trunk_config(t_dict[1])

f = open('result.txt', 'w')
a_c.extend(t_c)
cfg_str = '\n'.join(a_c)
f.write(cfg_str)
f.close()


