d = {}

def decorate(func):
    def wrapper(*args):
        key, value = (func(*args)[0], func(*args)[1])
        for i in range(len(key)):
            d[key[i]] = value[i]
    return wrapper


@decorate
def get_key_value(*args):
    return key, value

key = list(map(str, input().split()))
value = list(map(str, input().split()))

get_key_value(key, value)

print(*sorted(d.items()))
