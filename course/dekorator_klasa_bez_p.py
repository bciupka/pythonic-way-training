import functools


class dekorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print(f'Przed wywołaniem funkcji {self.f} z parametrami:', args, kwargs)
        r = self.f(*args, **kwargs)
        print(f'Po wywołaniu funkcji {self.f} w zwrócona:', r)
        return r

# tak napisany dekorator działa dla zwykłych funkcji

@dekorator
def f1():
    print('f1')
f1()

# niestey w klasie psuje się przekazywanie self
class A:
    @dekorator
    def m1(self):
        print('m1')

# a = A()
# a.m1(a)

# jak to naprawić?
class dekorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print(f'Przed wywołaniem funkcji {self.f} z parametrami:', args, kwargs)
        r = self.f(*args, **kwargs)
        print(f'Po wywołaniu funkcji {self.f} w zwrócona:', r)
        return r

    def __get__(self, instance, owner):
        return functools.partial(self, instance)

class A:
    @dekorator
    def m1(self):
        print('m1')

a = A()
a.m1()
