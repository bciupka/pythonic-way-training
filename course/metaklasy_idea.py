class A:
    atr = 'mama'

B = A

def C():
    return A()

b0 = A()
b1 = B()
b2 = C()

class A:
    atr = 'mama'
    def m1(self):
        print('A.m1')

def m1(self):
    print('A.m1')


d = {
    'atr': 'mama',
    'm1': m1
}

NewA = type('NewA', (), d)
a = NewA()
a.m1()

# nic nie robiąca metaklasa:
def pierwsza_meta(cls_name, inheritance, cls_dict):
    return type(cls_name, inheritance, cls_dict)

def wersjonuj_meta(cls_name, inheritance, cls_dict):
    cls_dict['version'] = '1.2.3'
    return type(cls_name, inheritance, cls_dict)

class A(metaclass=wersjonuj_meta):
    ...

print(A.version)
