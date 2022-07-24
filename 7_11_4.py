t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def decorate(func):
    def wrapper(*kwargs):
        res = func(*kwargs)
        x = ''.join(res)
        counter = 0
        while "--" in x:
            x = x.replace('--', '-')
        return x

    return wrapper


@decorate
def translate(s):
    lst = []
    for i in s:
        if ('a' <= i <= 'z') or (i == '!'):
            lst.append(i)
        elif i not in ": ;.,_-!":
            lst.append(t[i])
        else:
            lst.append('-')
    return lst


s = input().lower()

f = translate(s)

print(''.join(f))
