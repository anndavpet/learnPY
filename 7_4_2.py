def translate(s, sep='-'):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    lst = []
    for i in s:
        lst.append(sep)
        for k in i:
            if k != ' ' and 'а' <= k <= 'я':
                lst.append(t[k])
            else:
                lst.append(k)
    return ''.join(lst[1:])


s = input().lower().split()
res = translate(s)
res2 = translate(s, sep="+")
print(res)
print(res2)
