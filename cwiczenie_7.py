class Pracownik:
    __slots__ = ['imie', 'podstawa', 'nadg', '_konto']
    def __init__(self, imie='Jan', podstawa=20, nadg=40):
        self.imie = imie
        self.podstawa = podstawa
        self.nadg = nadg
        self._konto = 0

    def pracuj(self, ile):
        if ile <= 8:
            self._konto += ile * self.podstawa
        else:
            self._konto += 8 * self.podstawa + (ile - 8) * self.nadg

    def wyplata(self):
        akt = self._konto
        self._konto = 0
        return akt


class Kierownik(Pracownik):
    __slots__ = ['bonus']
    def __init__(self, bonus=200, *args):
        super().__init__(*args)
        self.bonus = bonus

    def pracuj(self, ile):
        super().pracuj(ile)
        if ile >= 10:
            self._konto += self.bonus


class Dyrektor(Kierownik):
    __slots__ = ['bonus_d']
    def __init__(self, bonus_d=200, *args):
        super().__init__(*args)
        self.bonus_d = bonus_d

    def pracuj(self, ile):
        super().pracuj(ile)
        if ile > 0:
            self._konto += self.bonus_d


def zatrudnij_zespol(ile_p, ile_k, ile_d):
    lista = []
    for _ in range(ile_p):
        lista.append(Pracownik())
    for _ in range(ile_k):
        lista.append(Kierownik())
    for _ in range(ile_d):
        lista.append(Dyrektor())
    return lista


if __name__ == '__main__':
    p = Pracownik('Jan', 20, 40)  # imie, stawka normalna, stawka nadgodzinowa
    p.pracuj(2)  # naliczy się 40, w sumie 40
    p.pracuj(8)  # naliczy się 160, w sumie 200
    p.pracuj(9)  # naliczy się 200, w sumie 400
    print(p.wyplata())  # 400
    print(p.wyplata())  # 0

    p = Kierownik(200, 'Jan', 20, 40)  # imie, stawka normalna, stawka nadgodzinowa
    p.pracuj(2)  # naliczy się 40, w sumie 40
    p.pracuj(8)  # naliczy się 160, w sumie 200
    p.pracuj(9)  # naliczy się 200, w sumie 400
    p.pracuj(12)  # naliczy się 8 * 20 + 4 * 40 + 200
    print(p.wyplata())  # 920
    print(p.wyplata())  # 0

    lista_p = zatrudnij_zespol(10, 3, 1)
    for p in lista_p:
        p.pracuj(0)
        p.pracuj(4)
        p.pracuj(8)
        p.pracuj(9)
        p.pracuj(11)
    f_plac = sum(p.wyplata() for p in lista_p)
    print(f_plac)
