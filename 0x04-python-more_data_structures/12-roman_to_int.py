#!/usr/bin/python3
def roman_to_int(roman_string):
    values={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    numbers = []
    for char in roman_string:
        numbers.append(values[char])
    if len(roman_string) == 1:
        return numbers[0]
    total = 0
    num1 = 0
    num2 = 0
    for num1, num2 in zip(numbers, numbers[1:]):
        if num1 >= num2:
            total += num1
        else:
            total -= num1
    return total + num2
