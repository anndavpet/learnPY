lst = list(map(str, input().lower().split()))

d = {lst[x] for x in range(len(lst)) if len(lst[x]) > 3}

print(len(d))