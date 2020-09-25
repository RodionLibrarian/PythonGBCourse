result = 0
while True:
    list = input('Введите числа через пробел или "." для выхода: ').split()
    for i in range(len(list)):
        if list[i] == '.':
            print(result)
            quit()
        else:
            result += int(list[i])
    print(result)

