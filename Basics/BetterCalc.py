
while True:

    try:

        num1 = float(input("Enter your first num: "))
        op = input("Enter operator: ")
        num2 = float(input("Enter your second num: "))

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        else:
            print("Invalid operator")
        print("\n")

    except ValueError:
        print("Sorry wrong numbers...(")

