def dodaj_str(cls):
    def tmp(self):
        return f'str reprezentacja {self.__class__.__name__}'
    cls.__str__ = tmp
    return cls

@dodaj_str
class A:
    ...


a = A()
print(a)

# napisać dekorator klasowy, który dodaje haszowanie

class haszuj:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __call__(self, cls):
        p1 = self.p1
        p2 = self.p2
        def tmp(self):
            return int(getattr(self, p1)) + int(getattr(self, p2))
        def tmp2(self, other):
            return hash(self) == hash(other)
        cls.__hash__ = tmp
        cls.__eq__ = tmp2
        return cls


@haszuj('atr1', 'atr2')
class A:
    def __init__(self, atr1, atr2, atr3):
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3

a1 = A(11,22,33)
a2 = A(11,22,44)

s = set()
s.add(a1)
s.add(a2)
print(s)