import random

rounds = int(input('How many rounds you want to play: '))
for j in range(rounds):

    top_of_range = input('Enter a number or Q to quit: ').lower()

    if top_of_range == 'q':
        break

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print('Please enter a number larger than 0 next time..')
            quit()
    else:
        print('Enter a number next time..')
        quit()

    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = input('Make a guess: ')
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print('Please enter a number next time..')
            continue

        if user_guess == random_number:
            print('You got it!')
            break
        elif user_guess > random_number:
            print('You were above the number!')
        else:
            print('You were below the number!')

    if guesses > 10:
        print(f'Noob you got it in {guesses} guesses!')
    elif guesses == 1:
        for i in range(13):
            print(f'WOOOOOOWWWWWW!!!!!!! You got it in first try!!!!!!!!!!!!!!!!!!!!')
    else:
        print(f'Congrats CHUNG!!! You got it in {guesses} guesses!')
