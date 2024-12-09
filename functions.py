# 1

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)

print(distance(1, 2, 3, 4))

#2
def power(a, n):
    b = a
    for i in range(n - 1):
        b = b * a

    return b


print(power(3, 2))


#3
def capitalize(word):
    first_lower = word[0]
    return first_lower.upper() + word[1:]


word = input()
print(capitalize(word))

#4
def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x = x * i

    return x

print(factorial(3))

#5
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(power(2,3))

#6
def print_reverse():
    number = int(input("Vvedite chislo (ne 0)"))
    if number == 0:
        return
    print_reverse()
    print(number)

print_reverse()