class A:
    def __getattr__(self, item):
        print('__getattr__', item)
        return super().__getattr__(item)

    def __getattribute__(self, item):
        print('__getattribute__', item)
        return super().__getattribute__(item)

    def __missing__(self, key):
        # słownik - jak nie ma klucza
        ...
    def __set
a = A()
print(a.__str__())
print(a.dupa)
