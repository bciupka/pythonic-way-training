# napisać metaklasę, która będzie implementować
# konwersję do str

'''
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
'''


def meta_repr(cls_name, inheritance, cls_dict):
    def _repr(self):
        return f'{cls_name} {inheritance}'
    cls_dict['__repr__'] = _repr
    return type(cls_name, inheritance, cls_dict)


class B(metaclass=meta_repr):
    a = []


if __name__ == '__main__':
    test = B()
    print(repr(test))