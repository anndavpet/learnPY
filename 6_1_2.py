"""
Вводятся данные в формате ключ=значение в одну строчку через пробел.
Необходимо на их основе создать словарь, затем проверить, существуют ли
в нем ключи со значениями: 'house', 'True' и '5' (все ключи - строки).
Если все они существуют, то вывести на экран ДА, иначе - НЕТ.

Sample Input:

вологда=город house=дом True=1 5=отлично 9=божественно
Sample Output:

ДА

"""

d = list(map(str, input().split()))

lst = []

for i in range(len(d)):
    lst.append(d[i].split('='))

x = dict(lst)

if ('house' in x) and ('True' in x) and ('5' in x):
    print('ДА')
else:
    print('НЕТ')


