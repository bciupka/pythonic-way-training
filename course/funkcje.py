def f1(x: int, y: int, *args: int, k=11, l=22, **kwargs: int) -> int:
    print(f'{x=}, {y=}')
    print(f'{args=}')
    print(f'{k=}, {l=}')
    print(f'{kwargs=}')
    return 33


# f1(1, 2)
# f1(1, 2, 3, 4, 5, 6, 7, 8, 9)
# r = f1(1, 2, 3, 4, 5, 6, 7, 8, 9, l=222, u=99, o=88, j=66)
# print(r)


# funkcja która może przyjąć dowolne parametry wejściowe
def f2(*args, **kwargs):
    print(f'{args=}')
    print(f'{kwargs=}')


# jak zabronić rpzekazywania parametrów słownikowych po nazwie:
def f3(x, y, *, k=11, l=22):
    print(f'{x=}, {y=}')
    print(f'{k=}, {l=}')


# f3(1,2, k=55, l=88)
# f3(1,2, 55, 88)

# parametry słownikowe bez wartości domyślnej:
def f4(x, y, *, k, l):
    print(f'{x=}, {y=}')
    print(f'{k=}, {l=}')


# f4(1, 2, l=3, k=4)

def f5(x, y):
    print(f'{x=}, {y=}')


def f5(x):
    print(f'{x=}')


# nie ma przeciążania!!!
# f5(1, 2)

x = 9


def f6():
    x = 99
    return x


# x = f6()
# print(x)

# __name__ = 'global name'
def f7():
    # __name__ = 'enclosing name'

    def f7_1():
        # __name__ = 'local name'
        print(__name__)

    f7_1()


# f7()

# wartość domyślna inichjuje się w momencie definiowania funkcji!!!
# bardzo nieintuicyjne!!!
def f8(i, x=[]):
    x.append(i)
    print(id(x), x)


# f8(1)
# f8(2)
# f8(3)

def f9(i, x=None):
    if x is None:
        x = []
    x.append(i)
    print(id(x), x)


# f9(1)
# x1 = []
# f9(2)
# x2 = []
# f9(3)

def f10():
    x = 999
    y = 888
    lista_f = []
    for z in range(3):
        def f10_1(z=z):
            print(x, y, z)

        lista_f.append(f10_1)
    return lista_f


lista_f = f10()
for f in lista_f:
    f()
print(lista_f[0].__closure__)
