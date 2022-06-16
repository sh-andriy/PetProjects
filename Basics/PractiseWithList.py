my_list = [1, 5, 7, 9, 69]
print(my_list)
my_list.insert(0, 'First')
my_list.append('last')
print(my_list)
del my_list[0]
my_list.pop()
print(my_list)
print(my_list.index(9))
test = int(input('Search in the list: '))
if test in my_list:
    print('Yes it is in list')
else:
    print('False')
