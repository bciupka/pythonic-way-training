s = {1, 2, 3, 4}
print(s)
s = {'ala',
     'ola',
     'ula'}
print(s)
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)
s.add(4.0)
print(s)
print(4 == 4.0)
s.add(5.0)
s.add(5)
print(s)
x = [1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 3, 5, 3, 34, 54, 5, 3, 3, 23, 23, 23, 54, 5, 5, 67, 7]
print(set(x))
# a co jeżeli chcę wartości unikalne ale bez zmiany kolejności
print({i: None for i in x}.keys())

print(set('abcdef'))
s1 = set('abcdef')
s2 = set('defghi')
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)
s = set()
s.add((1, 2, 3))
print(s)


class A:
    def __init__(self, atr1, atr2):
        self.atr1 = atr1
        self.atr2 = atr2

    # do poprawnego działania haszowania konieczna implementacja 2 metod:
    def __hash__(self):
        return hash((self.atr1, self.atr2))

    def __eq__(self, other):
        return self.atr1 == other.atr1 and self.atr2 == other.atr2


s = set()
a1 = A(112,222)
a2 = A(112, 222)
s.add(a1)
s.add(a2)
print(s)
# uwaga - obiekty są mutowalne!!!
a1.atr1 = 666
s.add(a1)
print(s)
