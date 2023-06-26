# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

line_array = []

vlan_num = int(input("Введите номер VLAN: "))

with open("CAM_table.txt") as f:
    for line in f:
        line = line.strip()
        if not line or not line[0].isdigit():
            continue
        line = line.split()
        if int(line[0]) == vlan_num:
            line_array.append([int(line[0]), line[1], line[3]])

line_array.sort()
for line in line_array:
    print("{:<9} {:20} {:5}".format(line[0], line[1], line[2]))