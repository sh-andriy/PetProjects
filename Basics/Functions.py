
def sayhi():
    print("Hello User")

print("Top")
sayhi()                 # Йде по черзі ряд 5-7 #
print("Bottom")

def sayhello(name, age):     # Ми вказали функції, те що при її викликанні тепер треба вказати ім'я та вік #
    print(f"Hello {name}, you are {age} years old")

sayhello("Steve", "13")
sayhello("John", "58")



def f1(x = 1, y = 2):
    x = x + y
    y += 1
    print(x, y)

f1(y = 2, x = 1)


my_list = [1, 5, 5, 5, 5, 1]
max_ = my_list[0]
index_of_max  = 0
for i in range(1, len(my_list)):
    if my_list[i] > max_:
        max_ = my_list[i]
        index_of_max = i
print(index_of_max)
