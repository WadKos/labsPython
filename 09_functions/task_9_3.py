# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    access_vlan = {}
    trunk_vlan = {}
    with open(config_filename) as f:
        current_interface = ""
        for line in f:
            if "interface" in line:
                current_interface = line.strip().split()[1]
            if "switchport access vlan" in line:
                access_vlan[current_interface] = int(line.strip().split()[3])
            if "switchport trunk allowed vlan" in line:
                vlan_list = [int(char) for char in line.strip().split()[4].split(",")]
                trunk_vlan[current_interface] = vlan_list

    res = (access_vlan, trunk_vlan)
    return res

print(get_int_vlan_map("config_sw1.txt"))