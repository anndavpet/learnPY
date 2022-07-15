def is_min(a, b):
    return a * b


n = list(map(int, input().split()))

print(is_min(max(n), min(n)))
