def is_simple(x):
    d = x -1
    if d < 0:
        return False

    while d > 1:
        if x % d == 0:
            return False
        d -= 1

    return True


a = [x for x in range(1, 11)]

b = filter(is_simple, a)

for i in b:
    print(i)

lst = ['Virginia', 'Florida', 'Trafalgar    ', 'Moscow']

b = filter(str.isalpha, lst)

print(tuple(b))