# https://stepik.org/lesson/567046/step/9?unit=561320

"""
Вводятся номера телефонов в формате:

номер_1 имя_1
номер_2 имя_2
...
номер_N имя_N

Необходимо создать словарь d, где ключами будут имена, а значениями - список номеров телефонов для этого имени. Обратите внимание, что одному имени может принадлежать несколько разных номеров. Полученный словарь вывести командой:

print(*sorted(d.items()))

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:

+71234567890 Сергей
+71234567810 Сергей
+51234567890 Михаил
+72134567890 Николай

Sample Output:

('Михаил', ['+51234567890']) ('Николай', ['+72134567890']) ('Сергей', ['+71234567890', '+71234567810'])
"""

import sys

# считывание списка из входного потока
lst = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst)

lst_1 = []

lst_2 = []

for i in range(len(lst)):
    x = lst[i].split()
    lst_2.append(x)
    y = [x[1]]
    y.append([])
    lst_1.append(y)
    
for i in range(len(lst_1)):
    x = lst_1[i][0]
    for j in range(len(lst_2)):
        y = lst_2[j][1]
        if x == y:
            lst_1[i][1].append(lst_2[j][0])
        
d = dict(lst_1)
print(*sorted(d.items()))

