class User:
    def __init__(self, last_name, first_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

print('Player1 info:\n')
name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = input('Enter your age: ')
player_1 = User(first_name=name, last_name=last_name, age=age)
print(player_1.first_name, player_1.last_name, player_1.age)


class Chungus:
    def __init__(self, name, age, weigh, favourite_food):
        self.name = name
        self.age = age
        self.weigh = weigh
        self.favourite_food = favourite_food

name = input('Enter chung name: ')
age = int(input('Enter chung age: '))
weigh = float(input('Enter chung weigh: '))
favourite_food = input('Enter chung favourite food: ')
chung_1 = Chungus(name=name, age=age, weigh=weigh, favourite_food=favourite_food)
print(chung_1.name, chung_1.age, chung_1.weigh, chung_1.favourite_food)

print('Player2 info:\n')
name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = input('Enter your age: ')
player_2 = User(first_name=name, last_name=last_name, age=age)
print(player_2.first_name, player_2.last_name, player_2.age)

name = input('Enter chung2 name: ')
age = int(input('Enter chung2 age: '))
weigh = float(input('Enter chung2 weigh: '))
favourite_food = input('Enter chung2 favourite food: ')
chung_2 = Chungus(name=name, age=age, weigh=weigh, favourite_food=favourite_food)
print(chung_2.name, chung_2.age, chung_2.weigh, chung_2.favourite_food)

if chung_1.weigh > chung_2.weigh:
    print(f'{chung_1.name} is more Damn than {chung_2.name}, she weighs {chung_1.weigh} kilograms')
elif chung_1.weigh < chung_2.weigh:
    print(f'{chung_2.name} is more Damn than {chung_1.name}, he weighs {chung_2.weigh} kilograms')
elif chung_1.weigh == chung_2.weigh:
    print(f'{chung_1.name} and {chung_2.name} has the same weigh')
else:
    print('Sorry smth is wrong')





