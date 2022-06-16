from typing import List
from operator import attrgetter


class Chungus:
    def __init__(self, name, age, weight, favourite_food):
        self.name = name
        self.age = age
        self.weight = weight
        self.favourite_food = favourite_food

    def __str__(self):
        return self.name

class User:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.chunguses: List[Chungus] = []

    def add_chungus(self, chung: Chungus) -> None:
        self.chunguses.append(chung)

    def __str__(self):
        return self.first_name


all_players = []

try:
    amount_users = int(input("Enter amount of Users: "))

    for i in range(amount_users):

        print(f'Player{i + 1} info:\n')
        name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        age = int(input('Enter your age: '))
        player = User(first_name=name, last_name=last_name, age=age)
        print(player.first_name, player.last_name, player.age)
        chung_amount = int(input('How many chungs you want to add: '))
        for j in range(chung_amount):

            name = input('Enter chung name: ')
            age = int(input('Enter chung age: '))
            weight = float(input('Enter chung weight: '))
            favourite_food = input('Enter chung favourite food: ')
            chung = Chungus(name=name, age=age, weight=weight, favourite_food=favourite_food)
            player.add_chungus(chung)
            print(chung.name, chung.age, chung.weight, chung.favourite_food)

        all_players.append(player)


except ValueError:
    print(ValueError)

a = User("Niko", "She", 20)
a.chunguses = [Chungus(name="Eula", age=5, weight=2.5, favourite_food="Nut"),
               Chungus(name="Albedo", age=5, weight=2.9, favourite_food="Apple")]

b = User("King", "She", 16)
b.chunguses = [Chungus(name="Razor", age=2, weight=2.7, favourite_food="Keder")]

all_players=[a, b]

player_biggest_chungus_pair = []

for player in all_players:
    biggest_player_chungus = player.chunguses[0]

    for chung in player.chunguses:
        if chung.weight > biggest_player_chungus.weight:
            biggest_chung = chung

    player_biggest_chungus_pair.append([player, biggest_player_chungus])


biggest_chung_player = player_biggest_chungus_pair[0][0]
biggest_chung = player_biggest_chungus_pair[0][1]

for player, chungus in player_biggest_chungus_pair:
    if chungus.weight > biggest_chung.weight:
        biggest_chung_player = player
        biggest_chung = chungus



print(f"""
Congratulation {biggest_chung_player.first_name}!!!
Your chungus {biggest_chung.name} are DAMN big and love to eat {biggest_chung.favourite_food}
)))) YAY!!!
""")




"""
знайти юзера в якого є найбільший чунг
Niko have biggest chung Eula that is 3kg DAMN!!! - winner
"""


'''
        if chung_1.weight > chung_2.weight:
            print(f'{chung_1.name} is more Damn than {chung_2.name}, she weights {chung_1.weight} kilograms (DAMN!!!!)')
        elif chung_1.weight < chung_2.weight:
            print(f'{chung_2.name} is more Damn than {chung_1.name}, he weights {chung_2.weight} kilograms (DAMN!!!!)')
        elif chung_1.weight == chung_2.weight:
            print(f'{chung_1.name} and {chung_2.name} has the same weight')
        else:
            print('Sorry smth is wrong')
        '''

'''
    def __gt__(self, other):
        if self.weight > other.weight:
            print(f'{player.first_name} have biggest chung {chung.name} that is {chung.weight} damn!!!')
        elif other.weight > self.weight:
            print(f'{player.first_name} have biggest chung {chung.name} that is {chung.weight} damn!!!')
        else:
            print('They has the same weight')
'''