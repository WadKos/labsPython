# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
read_file_name = argv[1]
write_file_name = argv[2]

with open(read_file_name) as f, open(write_file_name, 'w') as wf:
    for line in f:
        check = set(line.split(' ')).intersection(set(ignore))
        if line.strip() and not line[0] == "!" and not check:
            wf.write(line)