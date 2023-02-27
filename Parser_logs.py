import os
from os.path import isfile
from os.path import join
from random import randint

path_coul = os.getcwd()
onlyfiles = [f for f in os.listdir(path_coul) if isfile(join(path_coul, f))]
for i in onlyfiles:
    new_file = os.path.splitext(i)[0] + str(randint(1, 999)) + '.txt'
    if os.path.splitext(i)[1] != '.py' and os.path.splitext(i)[1] != '.exe' and os.path.splitext(i)[1] != '.txt':
        os.rename(i, new_file)
onlyfiles = [f for f in os.listdir(path_coul) if
             isfile(join(path_coul, f)) and os.path.splitext(f)[1] != '.py' and os.path.splitext(f)[1] != '.exe']
with open('coul_errors.txt', 'w', encoding='utf-8') as file:
    for i in onlyfiles:
        type_errors = {'SyntaxError': 0, 'OutofMemoryError': 0, 'RecursionError': 0}
        with open(i, 'r', encoding='utf-8') as coul_txt:
            for line in coul_txt:
                for m, n in type_errors.items():
                    if line.count(m) != 0:
                        type_errors[m] = type_errors[m] + line.count(m)
            for m, n in type_errors.items():
                if n != 0:
                    print(i, ':', m, ' - ', n, file=file)
