"""
Вводится натуральное число, которое может быть определено
простыми множителями 1, 2, 3, 5 и 7.
Необходимо разложить введенное число на указанные простые
множители и проверить, содержит ли оно множители 2, 3 и 5
(все указанные множители)? Если это так, то вывести ДА,
иначе - НЕТ.

Sample Input:

210

Sample Output:

ДА

"""

num = int(input())
list_simple = []
simple = 2
while num > 1:
    if num % simple == 0:
        list_simple.append(simple)
        num = num/simple
    else:
        simple += 1

X = set(list_simple)

Y = {2, 3, 5}

print('ДА' if (X & Y) == Y else 'НЕТ')