def show_menu(func):
    def wrapper(s):
        res = func(s)
        for key, value in enumerate(res):
            print(f"{key + 1}. {value}")

    return wrapper


@show_menu
def get_menu(s):
    return s.split()
