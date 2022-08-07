t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def df_decorate(chars='!?'):
    def func_decorate(func):
        def wrapper(s, *args, **kwargs):
            s = func(s)
            for i in s:
                if i in chars:
                    s = s.replace(i, '-')
            s_new = list(s)
            
            for j in range(len(s_new)-1):
                if '--' in ''.join(s_new):
                    del s_new[j]
                    
            s = ''.join(s_new)
            return s
            
        return wrapper
    return func_decorate


@df_decorate(chars="?!:;,. ")
def render(s, *args, **kwargs):
    for i in s:
        if ('a' <= i <= 'z'):
            continue
        elif i == ' ':
            s = s.replace(i, '-')
        elif i not in t:
            continue
        else:
            s = s.replace(i, t[i])
    return s

s = input()

f = render(s)
print(f)