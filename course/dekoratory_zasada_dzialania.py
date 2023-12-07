import functools
def dekorator(f):
    @functools.wraps(f)
    def nowa_f(*args, **kwargs):
        print(f'Przed wywołaniem funkcji {f} z parametrami:', args, kwargs)
        r = f(*args, **kwargs)
        print(f'Po wywołaniu funkcji {f} w zwrócona:', r)
        return r

    return nowa_f


@dekorator
def f1(x, y):
    print('f1', x, y)
    return x + y


# f1 = cos(f1)

print(f1)
print(f1(11, 22))
