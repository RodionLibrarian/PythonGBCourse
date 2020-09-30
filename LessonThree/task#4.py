def my_func(x, y):
    return 1 / x ** abs(y)


print(my_func(2, -4))


def my_func2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


print(my_func2(2, -4))
