lst = list(map(str, input().split()))

d = {}

for key, value in enumerate(lst[1:], int(lst[0])):
    d[key] = value

print(d[4])