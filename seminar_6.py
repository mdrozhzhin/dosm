variant = 11
phone_number1 = [8, 9, 1, 0, 4, 0, 2, 2, 5, 7, 8]
phone_number2 = [8, 9, 1, 9, 1, 0, 6, 1, 2, 6, 1]
numbers = [12, 24, 36, 48, 109, 187]


def multiply_by_number(number, multiplier):
    return number * multiplier


result_a = list(map(lambda x: multiply_by_number(x, variant + 7), numbers))
print(result_a)

result_b = list(map(lambda x: x * (variant + 7), numbers))
print(result_b)


result = list(map(lambda x, y: x * y, phone_number1, phone_number2))

print(result)


multiplied_numbers = [digit * variant for digit in phone_number1]

even_numbers = list(filter(lambda x: x % 2 == 0, multiplied_numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, multiplied_numbers))

print("Четные числа:", even_numbers)
print("Нечетные числа:", odd_numbers)


phone_number_str = '89104022578'

phone_numbers_int_div = list(map(lambda x: int(x) // variant, phone_number_str))
phone_numbers_float_div = list(map(lambda x: int(x) / variant, phone_number_str))

print("Целочисленное деление:", phone_numbers_int_div)
print("Дробное деление:", phone_numbers_float_div)
