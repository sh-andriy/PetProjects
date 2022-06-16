
def max_num(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

try:
    num1 = int(input("Enter ur firs num:"))
    num2 = input("Enter ur second num:")
    num3 = input("Enter ur third num:")


    num2 = int(num2)
    num3 = int(num3)

    print(max_num(num1, num2, num3))

except ValueError:
    print("Sorry wrong numbers")







