import sys
import time


class WorkWithFiles:

    def timer(func):
        def wrapper(self, *args, **kwargs):
            start = time.time()
            func(self, *args, **kwargs)
            total = time.time() - start
            print('Time: ', total)
            print(type(kwargs))
            for i in kwargs.values():
                if i == self.file_name:
                    print('I am Groot!')
            return func
        return wrapper

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    @timer
    def get_counters(self, arg="afsa"):
        text = self.file.read()
        amount_of_words = len(text.split())
        print("Custom text from arg", arg)
        print(f'Amount of words in file: {amount_of_words}')
        c1 = text.count('n')
        c2 = text.count('N')
        print(c1 + c2)

    @timer
    def __enter__(self):
        try:
            self.file = open(self.file_name)
            self.get_counters(arg=self.file_name)
        except FileNotFoundError:
            print('Sorry NO file!!!')
            self.__exit__(*sys.exc_info())
            sys.exit()
        return self

    @timer
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with WorkWithFiles(file_name='../../../../Andriy/Projects/PetProjects/FileManagement/data2.txt') as fil:
    fil.get_counters(arg="afsfaf")
