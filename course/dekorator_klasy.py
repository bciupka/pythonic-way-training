def dodaj_str(cls):
    def tmp(self):
        return f'str reprezentacja {self.__class__.__name__}'

    cls.__str__ = tmp
    return cls


@dodaj_str
class A:
    ...


a = A()


# print(a)


# napisać dekorator klasowy, który dodaje haszowanie

class haszuj:
    def __init__(self, *atrybuty):
        self.atrybuty = atrybuty

    def __call__(self, cls):
        atrybuty = self.atrybuty

        def _hash(self):
            return hash(tuple(getattr(self, a) for a in atrybuty))

        def _eq(self, other):
            return all(getattr(other, a) == getattr(self, a)
                       for a in atrybuty)

        cls.__hash__ = _hash
        cls.__eq__ = _eq
        return cls


class stringuj:
    def __init__(self, *atrybuty):
        self.atrybuty = atrybuty

    def __call__(self, cls):
        atrybuty = self.atrybuty

        def _repr(self):
            x = ', '.join(f'{a}={getattr(self, a)}' for a in atrybuty)
            return f'{cls.__name__}({x})'

        cls.__repr__ = _repr
        return cls


@stringuj('atr1', 'atr2', 'atr3')
@haszuj('atr1', 'atr2')
class A:
    def __init__(self, atr1, atr2, atr3):
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3


a1 = A(11, 22, 33)
a2 = A(11, 22, 44)

s = set()
s.add(a1)
s.add(a2)
print(s)
