def filter_lst(it):
    negative_numbers = [x for x in it if x < 0]
    zero_negative = [x for x in it if x >= 0]
    diapason = [x for x in it if 3 <= x <= 5]
    return negative_numbers, zero_negative, diapason


it = list(map(int, input().split()))

res = filter_lst(it)

print(*it)
print(*res[0])
print(*res[1])
print(*res[2])
