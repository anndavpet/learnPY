lst = list(map(str, input().lower().split()))
lst2 = []
for i in range(len(lst) - 1):
    if (lst[i][-1] == 'ъ') or (lst[i][-1] == 'ь') or lst[i][-1] == 'ы':
        if lst[i][-2] == lst[i+1][0]:
            lst2.append(1)
        else:
            lst2.append(0)
    elif lst[i][-1] == lst[i+1][0]:
        lst2.append(1)
    else:
        lst2.append(0)

flag = False

for i in range(len(lst2)):
    if lst2[i] == 0:
        flag = True

if flag:
    print('НЕТ')
else:
    print('ДА')
