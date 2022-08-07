from snake_case.constants import PERSON
from snake_case.functions import greet

greet(PERSON)


def df_decorator(chars='./-&@!#$%^&*()<>'):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)

            flag = False

            for i in chars:
                if i in res:
                    flag = True
                else:
                    return 'NO'

            return f'Decorator with parameters: ' + res

        return wrapper

    return func_decorator


@df_decorator('./-&@!#$%^&*()<>')
def get_list(s):
    return ''.join(s)


s = list(map(str, input().split()))

f = get_list(s)

print(f)



