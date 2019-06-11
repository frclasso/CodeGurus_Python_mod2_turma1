import functools, time

def slow_down(func):
    """Timer de 1 segundo após chamar a função"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(2)
        value = func(*args, **kwargs)
        return value
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print('Finish...')
    else:
        print(from_number)
        countdown(from_number - 1)


print(countdown(3))