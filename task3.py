# stack = []

# input = ["3", "5", "+"]

# for key in input:
#     if key in "+-*/":
#         b = stack.pop()
#         a = stack.pop()

#         if key == '+':
#             stack.append(a+b)
#         elif key == '-':
#             stack.append(a-b)
#         elif key == '*':
#             stack.append(a*b)
#         elif key == '/':
#             stack.append(int(a/b))
        
#     else:
#         stack.append(int(key))

# print(stack[0])
        

def count(inputs):
    stack = []

    for key in inputs:
        if key in "+-*/":
            b = stack.pop()
            a = stack.pop()

            if key == '+':
                stack.append(a+b)
            elif key == '-':
                stack.append(a-b)
            elif key == '*':
                stack.append(a*b)
            elif key == '/':
                stack.append(int(a/b))
            
        else:
            stack.append(int(key))
    return(stack[0])

print(count(["3", "5", "+"]))
print(count(["2", "1", "+", "3", "*"]))
print(count(["4", "13", "5", "/", "+"]))