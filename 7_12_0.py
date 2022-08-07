def df_decorator(start=5):
    def func_decorator(func):
        def wrapper(nums, *args, **kwargs):
            res = (func(nums) + start)
            return res

        return wrapper

    return func_decorator


# @df_decorator(5)
def render(nums):
    return sum(nums)


nums = list(map(int, input().split()))

f = df_decorator(start=5)
render = f(render)

df = render(nums)

print(df)
