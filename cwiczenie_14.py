class MM:
    d = {}

    def register(self, type_t, f):
        self.d[type_t] = f

    def __call__(self, *args, **kwargs):
        t = tuple(type(a) for a in args)
        f = self.d[t]
        return f(*args)

mm = MM()
def f1(x, y):
    return f'str f1({x}, {y})'
mm.register((str, int), f1)

def f1(x, y):
    return f'int f1({x}, {y})'
mm.register((int, int), f1)

print(mm('ala', 2))

# * 1. Rozbudować o bazowanie na typach wszystich parametrów pozycujnych
# 2. Co z metodą - tzn co jeżeli rejestruję metodę klasy
# 3. Wiele metod / funkcji