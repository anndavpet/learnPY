def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


lst = list(map(int, input().split()))

new_lst = []

for n in lst:
    if not is_even(n):
        new_lst.append(n)
    else:
        continue

res = is_even(n)
print(*new_lst)
