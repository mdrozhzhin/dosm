import math
from scipy.special import comb


def square_0(number):
    result = number ** 2
    return result


num = 5
print(f'Возвращаемый результат: {square_0(num)}')


def square_1(number):
    result = number ** 2
    print(f'Квадрат числа равен: {result}')


num = 5
print(f'Возвращаемый результат: {square_1(num)}')


def square_2(number):
    result = number ** 2
    print(f'Квадрат числа равен: {result}')
    return result


num = 5
print(f'Возвращаемый результат: {square_0(num)}')


def nums(x):
    nums_list = [x - 1, x + 1]
    print(nums_list)


nums(7)


def str_lower(string):
    words = string.split()
    lower_words = [word.lower() for word in words]
    print(lower_words)


str_lower('Я тут кое-что тестирую')


def my_log(list_of_numbers):
    logs = []
    for i in list_of_numbers:
        if i > 0:
            logs.append(math.log(i))
        else:
            logs.append(None)

    return logs


numbers = [1, 2, 3, 0, -1, 10]
logarithms = my_log(numbers)
print(logarithms)


def create_dictionary(name, age):
    if len(name) == len(age):
        result = dict(zip(name, age))
        return result
    else:
        print('Списки имеют разную длину')
        return {}


names = ['Василий', 'Геннадий', 'Инокентий']
ages = [25, 30, 35]
result_dict = create_dictionary(names, ages)
print(result_dict)

names2 = ['Альберт', 'Серафим']
ages2 = [40, 45, 50]
result_dict2 = create_dictionary(names2, ages2)
print(result_dict2)


def binom_prob(p, n, k):
    coef = comb(n, k)
    prob = coef * p ** k * (1 - p) ** (n - k)
    return prob


p = 0.5  # Вероятность успеха в одном испытании
n = 10  # Количество испытаний
k = 5  # Количество успехов
probability = binom_prob(p, n, k)
print(f'Вероятность получить {k} успехов из {n} испытаний с вероятностью успеха {p:.2f}: {probability}')


def all_sort(*args: object) -> object:
    int_numbers = list(args)
    sorted_numbers = sorted(int_numbers)
    return sorted_numbers


sorted_list = all_sort(5, 2, 7, 1, 9)
print(sorted_list)
