def is_correct(s):
    if len(s) < 6:
        return False
    else:
        return True


_input = list(map(str, input().split()))

lst = [i for i in _input if is_correct(i)]

print(*lst)
