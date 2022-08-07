# function read string
# decorator with parameters
# argument 'chars' in decorator

def df_decorator():
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)

            return res
        return wrapper
    return func_decorator


def get_list(*args):
    return args


s = input()

f = get_list(s)

print(f)