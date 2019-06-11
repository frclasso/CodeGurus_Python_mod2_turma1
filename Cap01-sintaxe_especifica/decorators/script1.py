


# def first(msg):
#     print(msg)
#
# first("Floripa Code Gurus")
#
# second = first("Hello Gurus")

def is_called():
    def is_returned():
        print('Hello Gurus')
    return is_returned()

is_called()

print()

def make_pretty(func):  # decoradora
    def inner():
        print('I got decorated')
        func()
    return inner()

def ordinary():  # decorada
    print('I am ordinary')

# 1a sitaucao
make_pretty(ordinary)

# 2a situacao

@make_pretty
def ordinary():
    print('I am ordinary')