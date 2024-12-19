def add(first, second, third):
    return first + second + third


def muinus(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return first // second


def print_sum():
    first = 5
    second = 7
    third = 4
    result = add(first, second, third)
    print(f'Сумма {first} и {second} и {third} равна {result}')


def print_minus():
    first = 35
    second = 7
    result = muinus(first, second)
    print(f'Разность {first} и {second} равна {result}')


def print_multiply():
    first = 111
    second = 111
    result = multiply(first, second)
    print(f'Произведение {first} и {second} равно {result}')


def print_divide():
    first = 666
    second = 111
    result = divide(first, second)
    print(f'Частное {first} и {second} равно {result}')
