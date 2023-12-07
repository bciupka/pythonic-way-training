class Czlowiek:
    __slots__ = [
        '_imie',
        '_nazwisko']

    def _set_imie_nazwisko(self, w):
        print('setter')
        self._imie, self._nazwisko = w.split()

    def _get_imie_nazwisko(self):
        print('getter')
        return f'{self._imie} {self._nazwisko}'

    imie_nazwisko = property(fget=_get_imie_nazwisko, fset=_set_imie_nazwisko)

    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko


class Czlowiek:
    __slots__ = [
        '_imie',
        '_nazwisko']

    @property
    def imie_nazwisko(self):
        print('getter')
        return f'{self._imie} {self._nazwisko}'

    @imie_nazwisko.setter
    def imie_nazwisko(self, w):
        print('setter')
        self._imie, self._nazwisko = w.split()

    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko


if __name__ == '__main__':
    c1 = Czlowiek('Ala Nowak')
    print(c1.imie_nazwisko)
    c1.imie_nazwisko = ('Adam Kowalski')
    print(c1.imie_nazwisko)
