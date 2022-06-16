
numbers = [2, 13, 155, 49, 65, 96, 69, 13]
friends = ["Eula", "Albedo", "Mykola", "Yuriy", "Nadia", "Andriy", "Bars"]
       #     0         1         2         3        4        5        6          #
friends.append("Chung") # Додасть до ліста ще одне ім'я #
print(friends)
friends.insert(1, "Chungus") # На місце першого елемента ставимо Чунгуса і всі інші зсуваються на право #
print(friends)
friends.remove("Mykola") # Забере з ліста Миколу #
print(friends)
# friend.clear() (очищує ліст)
# friends.pop() (Забирає останній елемент з ліста)
# friends.extend(numbers) # Додаєм до ліста з друзями ліст з цифрами #
print(friends.index("Yuriy")) # Показує індекс (номер) Юри #
print(friends.count("Albedo")) # Показує скільки разів є Альбедо в лісті #
print(numbers.count(13))

numbers.reverse()
print(numbers) # Реверсить ліст з цифрами #

friends.sort()
print(friends) # Розсотрує ліст в алфавітному порядку #

numbers.sort()
print(numbers) # Розсотрує ліст з цифр в порядку зростання #

friends2 = friends.copy()
print(friends2) # Ми до ліста friends2 скопіювали ліст friends #

