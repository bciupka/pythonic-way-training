import functools


class dekorator:
    def __init__(self, p1 = 11):
        self.p1 = p1
        # self.p2 = p2
        ...

    def __call__(self, f):
        @functools.wraps(f)
        def nowa_f(*args, **kwargs):
            print('parametry dekoratora:', self.p1, self.p2)
            print(f'Przed wywołaniem funkcji {f} z parametrami:', args, kwargs)
            r = f(*args, **kwargs)
            print(f'Po wywołaniu funkcji {f} w zwrócona:', r)
            return r

        return nowa_f


@dekorator()
def f1(x, y):
    print('f1', x, y)
    return x + y


print(f1(11, 22))
