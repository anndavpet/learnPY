nums = list(map(int, input().split()))

lst = []

i = 0

while nums:
    x = min(nums)
    lst.append(x)
    nums.remove(x)
    i += 1

print(*lst)