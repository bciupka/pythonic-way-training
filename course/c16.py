# napisać metaklasę, która będzie implementować
# konwersję do str
# nic nie robiąca metaklasa:
def auto_slots(cls_name, inheritance, cls_dict):
    new_d = {}
    slots = []
    for atr_name, atr_val in cls_dict.items():
        new_d[atr_name] = atr_val
        if isinstance(atr_val, property):
            slots.append(f'_{atr_name}')
    new_d['__slots__'] = slots
    return type(cls_name, inheritance, new_d)


class Czlowiek(metaclass=auto_slots):

    def _set_imie_nazwisko(self, w):
        self._imie_nazwisko = w

    def _get_imie_nazwisko(self):
        return self._imie_nazwisko

    imie_nazwisko = property(fget=_get_imie_nazwisko, fset=_set_imie_nazwisko)

    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko


a = Czlowiek('Ala Nowak')
a.imie_nazwisko = 'Pawel Kowal'
a.inny = 1222
