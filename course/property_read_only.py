class Czlowiek:
    __slots__ = [
        'imie',
        'nazwisko']
    @property
    def imie_nazwisko(self):
        print('getter')
        return f'{self.imie} {self.nazwisko}'


    def __init__(self, imie, nazwisko):
        self.imie  = imie
        self.nazwisko = nazwisko


if __name__ == '__main__':
    c1 = Czlowiek('Ala', 'Nowak')
    print(c1.imie_nazwisko)
