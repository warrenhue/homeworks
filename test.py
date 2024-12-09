def factorial (i):
    res = 1

    for j in range (1, i+1):
        res = res*j
    return(res)

num = int(input())
sum = 1

for i in range (2, num+1):
    sum = sum + factorial(i)

print(sum)