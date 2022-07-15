def get_v(a, b, c, verbose=True):
    if verbose:
        print(f'a = {a}, b = {b}, c = {c}')
    return a * b * c


v = get_v(1, 2, 3, verbose=False)
print(v)
