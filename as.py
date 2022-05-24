n = int(input())

lst = [['1'] * n for i in range(n)]

for i in range(len(lst)):
    lst[i][-1] = 5
    print(*lst[i])

