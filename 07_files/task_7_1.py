# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

with open("ospf.txt") as f:
    for line in f:
        line = line.replace(',','')
        line = line.strip()
        line = line.replace('[','').replace(']','')
        ospf_list = line.split()
        print(template.format(ospf_list[1], ospf_list[2], ospf_list[4], ospf_list[5], ospf_list[6]))

