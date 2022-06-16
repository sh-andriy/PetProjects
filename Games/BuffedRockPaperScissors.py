import random

user_wins = 0
computer_wins = 0

combinations = {
    # link to idea https://www.umop.com/rps7.htm
    'rock': ['scissors', 'fire', 'sponge'],
    'water': ['rock', 'fire', 'scissors'],
    'air': ['water', 'rock', 'fire'],
    'paper': ['air', 'water', 'rock'],
    'sponge': ['paper', 'air', 'water'],
    'scissors': ['sponge', 'paper', 'air'],
    'fire': ['scissors', 'sponge', 'paper']
}


options = list(combinations.keys())

while True:
    user_input = input(f'Type {"/".join(options)} or Q to quit: ').lower()

    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, len(combinations)-1)

    #   rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]  # computer already know
    print(f'Computer picked {computer_pick}.')

    lose_option_for_pc = combinations[computer_pick]

    if user_input in lose_option_for_pc:
        print("You lost!")
        computer_wins += 1
    elif user_input == computer_pick:
        print("Draw!")
        user_wins = user_wins
        computer_wins = computer_wins
    else:
        print("You won!")
        user_wins += 1

print(f'You won {user_wins} times.')
print(f'The computer won {computer_wins} times.')
if user_wins > computer_wins:
    print(f'The winner is Chung with {user_wins} wins >_<')
elif user_wins < computer_wins:
    print(f'The winner is Computer with {computer_wins} wins). It is just smarter than you!LOL')
else:
    print('It is a Draw!')
print('Goodbye!')
