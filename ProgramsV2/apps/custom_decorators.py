import time


def show_timing(func):
    def wrapper(method_name):
        start = time.time()
        result = func(method_name)
        end = time.time()
        print("{} time is - {} s.".format(method_name, end - start))
        return result
    return wrapper
