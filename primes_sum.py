
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    summa = 0
    for i in range(2, n + 1):
        if is_prime(i):
            summa += i
    return summa

n = int(input())
sum = sum_of_primes(n)
print(sum)