class A:
    __slots__ = [
        '_dlugosc',
        '_szerokosc'
    ]
    atr1 = 111

    def _set_dlugosc(self, w):
        self._dlugosc = w

    def _get_dlugosc(self):
        return self._dlugosc

    dlugosc = property(fget=_get_dlugosc, fset=_set_dlugosc)

    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self._szerokosc = szerokosc

    def m1(self):
        print('jestem A.m1')

    @classmethod
    def cm1(cls):
        print('jestem metodą klasową')

    def cm2(self):
        print('jestem metodą instancyjną ale nie używam instancji', self.__class__)

    @staticmethod
    def sm1():
        print('jestem metodą statyczną')


a1 = A(222, 444)
a2 = A(333, 777)
print(a1.atr1, a2.__class__.atr1, A.atr1)
a1.__class__.atr1 = 444
print(a1.atr1, a2.atr1, A.atr1)
a1.m1()
print(a1._szerokosc)

# print(a1.dlugosc, a2.dlugosc)
# a1.dlugosc = 444
# print(a1.dlugosc, a2.dlugosc)
# print(a1.__dir__())
