class MojDeskryptor:
    # def __init__(self, atr_name):
    #     print('MojDeskryptor.__init__', atr_name)
    #     self._atr_name = atr_name

    def __set_name__(self, owner, name):
        print('__set_name__', self, owner, name)
        self._atr_name = f'_{name}'

    def __get__(self, instance, owner):
        print('__get__', instance, owner)
        return getattr(instance, self._atr_name)

    def __set__(self, instance, value):
        print('__set__', instance, value)
        setattr(instance, self._atr_name, value)


class A:
    atr1 = MojDeskryptor()


a1 = A()
a1.atr1 = 111
a1.atr1 = 222
a1.atr1 = 333

a2 = A()
a2.atr1 = 777
a2.atr1 = 888
a2.atr1 = 999

