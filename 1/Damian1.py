#!/usr/bin/python3

with open("input.txt") as file:
    numbers = []
    for _, line in enumerate(file):
        allDigits = []
        for char in line:
            if char.isdigit():
                allDigits.append(int(char))
                print(allDigits)
        number = allDigits[0] * 10 + allDigits[-1]
        numbers.append(number)
    print(sum(numbers))