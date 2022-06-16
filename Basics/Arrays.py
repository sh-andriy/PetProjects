try:
    numbers = []
    print(len(numbers))
    numbers.append(int(5))
    print(len(numbers))
    numbers.append(6)
    numbers.append(7)
    numbers.append(8)
    numbers.append(100)
    print(numbers)
    numbers.remove(7)
    print(numbers)
    numbers.pop(1)
    print(numbers)
    print(numbers.index(100))
    print(len(numbers))
except ValueError:
    print(ValueError)