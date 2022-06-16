
while True:
    try:
        input_string = str(input('Enter some words or smth: '))
        print(f'\nThe original string is: {input_string}')

        amount_of_words = len(input_string.split())
        print(f'The number of words in string are: {str(amount_of_words)}')

        amount_of_symbols = len(input_string)
        print(f'The number of letters in string incl spaces are: {str(amount_of_symbols)}')

        counter1 = input_string.count('N')
        counter2 = input_string.count('n')

        print(f'The number of N and n are: {counter1 + counter2}')

        input_counter = 0
        for i in input_string:
            if i.islower():
                input_counter = input_counter + 1
        print(f'n = {input_counter}')

        count = len([elem for elem in input_string if elem.isupper()])
        print(f'N = {count}\n')
    except ValueError:
        print("SORRY ERROR!")






