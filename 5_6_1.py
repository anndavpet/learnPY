
# https://stepik.org/lesson/567042/step/3?unit=561316

import sys

lst = list(map(str.strip, sys.stdin.readlines()))

lst_r = [lst[i].replace(' ', '-') for i in range(len(lst))]


j = 0

res = []

while j < len(lst_r):
    x = lst_r[j]
    j += 1
    while x.count('--'):
        x = x.replace('--', '-')
    res.append(x)

print(*res, sep='\n')
        

