import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        #aqui tem uma ação
        value = func(*arg, **kwargs)
        # aqui tem outração
        return value
    return wrapper_decorator()