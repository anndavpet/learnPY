"""
Вводится строка, содержащая латинские символы, пробелы и
цифры. Необходимо выделить из нее все неповторяющиеся
цифры (символы от 0 до 9) и вывести на экран в одну строку
через пробел их в порядке возрастания значений.
Если цифры отсутствуют, то вывести слово НЕТ.

Sample Input:

Python 3.9.11 - best language!

Sample Output:

1 3 9

"""

s = list(map(str, input()))

flag = False

for i in s:
    if i.isdigit():
        flag = True

if flag:
    x = [x for x in s if x.isdigit()]
    print(*sorted(set(x)))
else:
    print('НЕТ')
