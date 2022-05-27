# https://stepik.org/lesson/567046/step/4?unit=561320
"""
Вводятся данные в формате ключ=значение в одну строчку через пробел.
Значениями здесь являются целые числа (см. пример ниже).
Необходимо на их основе создать словарь d с помощью функции dict()
и вывести его на экран командой:

print(*sorted(d.items()))

Sample Input: one=1 two=2 three=3

"""

d = list(map(str, input().split()))

lst = []

for i in range(len(d)):
    lst.append(d[i].split('='))

for j in range(len(lst)):
    lst[j][1] = int(lst[j][1])

x = dict(lst)

print(*sorted(x.items()))