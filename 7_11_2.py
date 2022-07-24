def decorate(func):
    def wrapper(*kwargs):
        return sorted(func(*kwargs))
    return wrapper


@decorate
def get_list():
    lst = list(map(int, input().split()))
    return lst



lst = get_list()


print(*lst)
