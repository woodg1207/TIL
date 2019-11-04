def hello(func):
    def wrapper():
        print('HIhi')
        func()
        print('hahaha')
    return wrapper

@hello
def bye():
    print('byebye')

bye()