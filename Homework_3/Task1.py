def dive_nums(a, b):
    if b == 0:
        return "You can notdivide to 0!"
    else:
        return a / b


a = float(input("a: "))
b = float(input("b: "))
print(dive_nums(a, b))