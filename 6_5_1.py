"""
Вводятся два списка целых чисел каждый с новой строки
(в строке наборы чисел через пробел).
Необходимо выбрать и отобразить на экране уникальные числа,
присутствующие в первом списке, но отсутствующие во втором.
Результат выведите на экран
в виде строки чисел, записанных по возрастанию через пробел.
"""

X = set(map(int, input().split()))
Y = set(map(int, input().split()))

print(*sorted(X - Y))