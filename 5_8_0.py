a = list(map(str, input().split()))

lst = [[a[i-1], int(a[i])] for i in range(1, len(a), 2)]

print(lst)