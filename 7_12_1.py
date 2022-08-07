def df_decorator(tag='div'):
    def func_decorator(func):
        def wrapper(s, *args, **kwargs):
            res = f'<{tag}>{func(s)}</{tag}>'
            return res
        
        return wrapper
    return func_decorator


@df_decorator(tag='div')
def render(s):
    return s.lower()


s = input()

f = render(s)
print(f)
