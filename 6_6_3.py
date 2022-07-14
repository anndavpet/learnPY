s = list(map(str, input().lower().split()))

x = {s[x]: s.count(s[x]) for x in range(len(s))}

print(x['и'] if 'и' in x else 0)