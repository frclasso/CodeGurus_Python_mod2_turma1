import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # aqui tem uma acao
        value = func(*args, **kwargs)
        # aqui tem outra acao
        return value
    return wrapper_decorator()