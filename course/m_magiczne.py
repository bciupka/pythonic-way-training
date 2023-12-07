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

    def __repr__(self):
        return f'R: {self.__class__.__name__} {self.nr_rej} w ({self._x}, {self._y})'

    def __str__(self):
        return f'S: {self.__class__.__name__} {self.nr_rej} w ({self._x}, {self._y})'

    # delegowanie z funkcji globalnych
    def __len__(self):
        return 444

    # konwersje
    def __float__(self):
        return 55.6

    # konwersja do bool - zazwyczaj poważna mina - nie używać!!!
    def __bool__(self):
        return False

    # konstruktor __init__

    # destruktor __del__
    # UWAGA: 1. Nie ma gwaracji wywołania!!!
    #        2. W trakcie wywołania destruktora obiekt może być częściowo już zniszczony

    def __del__(self):
        print('Obiekt jest właśnie kasowany!!!')
        # if hasattr(self, 'jakis_atrybut'):
        #     print('to czyszczę')

    # woła się zawsze
    def __getattribute__(self, item):
        print('__getattribute__', item)
        return super().__getattribute__(item)

    # woła się jeżeli atrybut nie znaleziony
    def __getattr__(self, item):
        print('__getattr__', self, item)
        return 55

    # in
    def __contains__(self, item):
        ...

    # dostęp po indeksie lub slicing []
    def __getitem__(self, item):
        ...

    # haszowanie
    def __hash__(self):
        ...
    def __eq__(self, other):
        ...

    # generator / iterator
    def __iter__(self):
        ...
    def __next__(self):
        ...

    # przeciążanie operatorów

    # używany w sortowaniu
    def __lt__(self, other):
        return False

    # +=
    def __iadd__(self, other):
        print('+=')

if __name__ == '__main__':
    s = Spychacz('kr12345')
    # print(s)  # Spychacz kr12345 w (0, 0)
    # s.jedz(10)
    # print(s)  # Spychacz kr12345 w (0, 10)
    # s.skrec_w_prawo()
    # s.jedz(10)
    # print(s)  # Spychacz kr12345 w (10, 10)
    # s.skrec_w_prawo()
    # s.jedz(10)
    # print(s)  # Spychacz kr12345 w (0, 10)
    # s.skrec_w_prawo()
    # s.jedz(10)
    # print(s)  # Spychacz kr12345 w (0, 0)
    # print([s])
    # print(len(s))
    #
    # # można ale czy trzeba?
    # print(float(s))
    #
    # # uwaga na kowersje do bool ponieważ:
    # if s:
    #     print('s istnieje')
    # else:
    #     print('s nie istnieje')
    #
    # del(s)

    # print(s.nr_rej)
    print(s.asdasdas)

    # wolno zapinplementować dodawanie pychacz ale czy warto?
    # s + s

    # fajne przeciążanie operatorów:
    import pathlib
    # ścieżka do venv względem bieżącego pliku
    p1 = pathlib.Path(__file__).parent / 'venv'

    s += 1