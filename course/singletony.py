class Singleton:
    type_dict = {}

    def __new__(cls, *args, **kwargs):
        if cls not in Singleton.type_dict:
            Singleton.type_dict[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return Singleton.type_dict[cls]


class Foo(Singleton):
    def __init__(self):
        print('__init__')



# brzydko - 2 razy wołany init
# f1 = Foo()
# f2 = Foo()
# print(f1 is f2)

# to może klasa wewnętrzna
class MyPrecious:
    class __MyPrecious:
        def __init__(self, arg):
            self.val = arg
            self.s = {1: 11, 2: 22}

        def init(self, arg):
            self.val = arg

        def __str__(self):
            return f'{repr(self)} {self.val}'

        def __getitem__(self, item):
            return self.s[item]

        def get_val(self):
            return self.val

    instance = None

    def __init__(self, *args, **kwargs):
        if not MyPrecious.instance:
            # Tu trzeby się zsynchronizować na obiekcie MyPrecious
            MyPrecious.instance = MyPrecious.__MyPrecious(*args, **kwargs)
        else:
            MyPrecious.instance.init(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __str__(self):
        return str(MyPrecious.instance)

    def __getitem__(self, item):
        return MyPrecious.instance[item]

# w miarę działa, ale 'is' nie działa i trzeba implementować metody magiczne

# x1 = MyPrecious(12)
# print(id(x1), x1)
# x2 = MyPrecious(12)
# print(id(x2), x2)
# print(x1.get_val(), x2.get_val())
# print(x1 is x2)


def singleton(class_):
    instances = {}

    # to też nie pomoże
    # @functools.wraps(class_)
    def getinstance(*args, **kwargs):
        return instances.setdefault(class_, class_(*args, **kwargs))

    return getinstance
#
#
@singleton
class MyClass():
    xx = 99

    @classmethod
    def m1(cls):
        print(cls.xx)


# a = MyClass()
# a.m1()
# b = MyClass()
# b.m1()
# print(a is b)
# a.__class__.m1()
# no ale niestety klasowe metody wołane przez nazwę klasy będą się wywalać
# MyClass.m1()
#

# Najlepsza implementacja - na metaklasach
# jak bonus coś w wersji a'la Flyweight
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(args, **kwargs)
        if (cls, args[0]) not in cls._instances:
            cls._instances[(cls, args[0])] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[(cls, args[0])]


# coś ala Flyweight
class MyClass(metaclass=Singleton):
    def __init__(self, par1):
        pass


a = MyClass(11)
b = MyClass(22)
print(a is b)

a = MyClass(11)
b = MyClass(11)
print(a is b)

# a jakby tak:
# moduły importują się tylko raz, więc zachowują się jak singleton:
# - zmienne globalne jako atrybuty
# - funkcje jako metody

# import moj_singleton
# import moj_singleton
