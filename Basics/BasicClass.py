class Chef:

    def make_chicken(self):
        print('making a chicken')

    def make_salad(self):
        print('making salad')

    def make_special_dish(self):
        print('making bbq ribs')


# chef_a = Chef()
# chef_a.make_salad()

class Parent:
    def __init__(self, param):
        self.v1 = param

class Child(Parent):
    def __init__(self, param):
        super().__init__(param)
        self.v2 = param


obj = Child(11)
print("%d %d" % (obj.v1, obj.v2))


counter = 1

def a():
    global counter
    for i in (1, 2, 3):
        counter += 1

a()
print(counter)


class A:
    def __str__(self):
        return "A"

class B(A):
    def __init__(self):
        super().__init__()

class C(B):
    def __init__(self):
        super().__init__()

def main():
    b = B()
    a = A()
    c = C()
    print(a, b, c)

main()

x = 2
y = 1
x *= y + 1
print(x)

nums = set([1, 1, 2, 3, 3, 3, 4])
print(len(nums))
