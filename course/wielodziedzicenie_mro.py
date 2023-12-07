class A:
    def m1(self):
        print('A.m1')

class B(A):
    # def m1(self):
    #     print('B.m1')
    #     super().m1()
    ...


class C:
    def m1(self):
        print('C.m1')


class D(B, C):
    def m1(self):
        i = self.__class__.__mro__.index(C) - 1
        print(i, self.__class__.__mro__[i])
        super(self.__class__.__mro__[i], self).m1()
        print('D.m1')
    ...


d = D()
print(D.__mro__)
d.m1()
