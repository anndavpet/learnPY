# https://stepik.org/lesson/567046/step/5?unit=561320
"""
На вход программы поступают данные в виде набора строк в формате: 

ключ1=значение1
ключ2=значение2
...
ключN=значениеN

Ключами здесь выступают целые числа (см. пример ниже). Необходимо их преобразовать в словарь d (без использования функции dict()) и вывести его на экран командой:

print(*sorted(d.items()))

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

5=отлично
4=хорошо
3=удовлетворительно

Sample Output:

(3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')
"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

lst = []

for i in range(len(lst_in)):
    lst.append(lst_in[i].split('='))

for j in range(len(lst)):
    lst[j][0] = int(lst[j][0])

x = dict(lst)

print(*sorted(x.items()))