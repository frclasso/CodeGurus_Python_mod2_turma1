def first(msg):
    print(msg)


first('Floripa code gurus')


second = first('Hello Gurus')


print()


def is_called():
    def is_returned():
            print('Hello Gurus')
    return is_returned()


is_called()

print()


def make_pretty(func):
    def inner():
        print('I got decorated')
        func()
    return inner()


def ordinary():
    print('I am ordunary')


make_pretty(ordinary)

# decorator

print()

@make_pretty
def ordinary():
    print('I am ordinary')