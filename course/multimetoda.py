import functools
import typing
from pprint import pprint


class MM:
    def __init__(self, is_bound):
        self._d = {}
        self._is_bound = is_bound

    def register(self, f):
        tt = tuple(typing.get_type_hints(f).values())
        if tt[0] == typing.Self:
            tt = tt[1:]
        self._d[tt] = f

    def __call__(self, *args, **kwargs):
        tt = tuple(type(a) for a in args)
        if self._is_bound:
            tt = tt[1:]
        f = self._d[tt]
        return f(*args)

    def __repr__(self):
        return f'MM({self._d})'


class mm_dekorator:
    _d = {}

    def __init__(self, is_bound=True):
        self._is_bound = is_bound

    def __call__(self, f):
        if f.__name__ not in self.__class__._d:
            self.__class__._d[f.__name__] = MM(self._is_bound)
        mm = self.__class__._d[f.__name__]
        mm.register(f)
        pprint(self.__class__._d)

        @functools.wraps(f)
        def tmp_f(*args, **kwargs):
            return mm(*args, **kwargs)

        return tmp_f


class A:
    @mm_dekorator()
    def f1(self: typing.Self, x: str, y: str):
        return f'str, str f1({x}, {y})'

    @mm_dekorator()
    def f1(self: typing.Self, x: int, y: int):
        return f'int, int f1({x}, {y})'

    @mm_dekorator()
    def f2(self: typing.Self, x: str, y: str):
        return f'str, str f2({x}, {y})'

    @mm_dekorator()
    def f2(self: typing.Self, x: int, y: int):
        return f'int, int f2({x}, {y})'


a = A()
print(a.f1('ala', 'aaa'))
print(a.f1(12, 22))

print(a.f2('ala', 'aaa'))
print(a.f2(12, 22))

# * 1. Rozbudować o bazowanie na typach wszystich parametrów pozycujnych
# * 2. Co z metodą - tzn co jeżeli rejestruję metodę klasy
# 3. Wiele metod / funkcji

