def is_palindrom(stroka):
    left = 0
    right = len(stroka) - 1

    while left < right:
        if stroka[left] != stroka[right]:
            return False
        left += 1
        right -= 1
    
    return True

input_string = input()
if is_palindrom(input_string):
    print("Палиндром")
else:
    print("Не палиндром")
