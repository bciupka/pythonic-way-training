# Napisać klasę Spychacz

class Spychacz:
    __slots__ = [
        '_x',
        '_y',
        'nr_rej',
        '_kierunek'
    ]

    def __init__(self, nr_rej):
        # jak zapisywać pozycję i kierunek???
        self.nr_rej = nr_rej
        self._x = 0
        self._y = 0
        self._kierunek = (0, 1)

    def jedz(self, ile_k):
        self._x += self._kierunek[0] * ile_k
        self._y += self._kierunek[1] * ile_k

    def skrec_w_prawo(self):
        """
        0, 1
        1, 0
        0, -1
        -1, 0
        """
        self._kierunek = (self._kierunek[1], -self._kierunek[0])

    def wypisz(self):
        print(f'{self.__class__.__name__} {self.nr_rej} w ({self._x}, {self._y})')


if __name__ == '__main__':
    s = Spychacz('kr12345')
    s.wypisz()  # Spychacz kr12345 w (0, 0)
    s.jedz(10)
    s.wypisz()  # Spychacz kr12345 w (0, 10)
    s.skrec_w_prawo()
    s.jedz(10)
    s.wypisz()  # Spychacz kr12345 w (10, 10)
    s.skrec_w_prawo()
    s.jedz(10)
    s.wypisz()  # Spychacz kr12345 w (0, 10)
    s.skrec_w_prawo()
    s.jedz(10)
    s.wypisz()  # Spychacz kr12345 w (0, 0)
