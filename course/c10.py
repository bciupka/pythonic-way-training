# Napisać włąsny deskryptor, który pamięta historię wartości atrybutu
# za każdą zmiana wartości printujemy historię
import collections


class HistoryDescriptor:

    def __init__(self):
        self._h = collections.defaultdict(list)

    def get_history(self, instance):
        return self._h[id(instance)]

    def __set_name__(self, owner, name):
        self._atr_name = f'_{name}'

    def __get__(self, instance, owner):
        print('getter', instance)
        if instance:
            return getattr(instance, self._atr_name)
        else:
            return self

    def __set__(self, instance, value):
        self._h[id(instance)].append(value)
        print(self._h)
        setattr(instance, self._atr_name, value)


class A:
    atr1 = HistoryDescriptor()
    atr2 = HistoryDescriptor()
    atr3 = HistoryDescriptor()

a1 = A()
a1.atr1 = 111
a1.atr1 = 222
a1.atr1 = 333

a2 = A()
a2.atr1 = 777
a2.atr1 = 888
a2.atr1 = 999

print(A.atr1.get_history(a1))
print(A.atr1.get_history(a2))