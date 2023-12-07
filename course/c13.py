# napisać metaklasę, która będzie implementować
# konwersję do str
# nic nie robiąca metaklasa:
def proste_str(cls_name, inheritance, cls_dict):
    def _repr(self):
        return f'{type(self).__name__}()'
    cls_dict['__repr__'] = _repr
    cls_dict['__str__'] = _repr
    return type(cls_name, inheritance, cls_dict)

class A(metaclass=proste_str):
    ...

a = A()
print(a)
print([a])