def is_prost(x):
    d = x - 1
    if d < 0:
        return False

    while d > 1:
        if x % d == 0:
            return False
        d -= 1

    return True


a = list(range(1, 11))

b = filter(is_prost, a)

lst = tuple(b)

print(lst)
