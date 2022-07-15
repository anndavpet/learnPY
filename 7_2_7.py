def is_len_string(s):
    return s, len(s)


lst = list(map(str, input().split()))

d = {}

for i in lst:
    d[is_len_string(i)[0]] = is_len_string(i)[1]

a = sorted(d, key=lambda x: d[x])
print(*a)
