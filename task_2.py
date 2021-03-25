def program(num):
    if num % 3 == 0:
        return '$$'
    elif num % 5 == 0:
        return '@@'
    elif num % 3 == 0 and num % 5 == 0:
        return '$$'
    else:
        return num


for num in range(11, 80):
    print(program(num))
