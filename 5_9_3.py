# https://stepik.org/lesson/567045/step/5?unit=561319
"""
Повторите задачу с транспонированием прямоугольной матрицы
с помощью list comprehension, изложенной в видео-уроке к этой практике.
На вход поступает таблица целых чисел, на выходе нужно отобразить эту же таблицу
в транспонированном виде (строки заменяются на столбцы), используя команду:

for row in A:
    print(*row)
    
где A - транспонированный двумерный список.
Желательно сделать эту задачу не пересматривая видео.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки. 
"""

import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
matr = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)

def transpose(matr):
    res=[]
    n=len(matr)
    m=len(matr[0])
    for j in range(m):
        tmp=[]
        for i in range(n):
            tmp=tmp+[matr[i][j]]
        res=res+[tmp]
    return res

x = transpose(matr)

for i in range(len(x)):
    print(*x[i])