def func_show(func):
    def wrapper(*args, **kwargs):
        res = func(*args)
        print(f"Площадь прямоугольника: {res}")

    return wrapper


def get_sq(a, b):
    S = a * b
    return S
