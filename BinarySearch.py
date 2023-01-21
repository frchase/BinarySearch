from math import log2


def factorial(x):

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))

target = 9.46E14
max_1 = 6E30
min = 0 
num = 0

while max_1 >= min:
    num = (max_1 + min) // 2
    if log2(num) * num > target:
        max_1 = num - 1
    elif target > log2(num) * num:
        min = num + 1

print(num)





