# Zaimplementować klasę Pracownik
from pprint import pprint

import faker
import abc


class Pracownik_Abstract(metaclass=abc.ABCMeta):
    def wyplata(self):
        # tmp = self._zarobki
        # self._zarobki = 0
        # return tmp
        try:
            return self._zarobki
        finally:
            self._zarobki = 0

    @abc.abstractmethod
    def pracuj(self, ile_h):
        ...

    def __str__(self):
        return f'S: {self.__class__.__name__}({self.imie}, i coś jeszcze...)'

    def __repr__(self):
        return f'R: {self.__class__.__name__}({self.imie})'


class Pracownik(Pracownik_Abstract):
    __slots__ = [
        'imie',
        'stawka_norm',
        'stawka_nad',
        '_zarobki'
    ]

    def __init__(self, *, imie, stawka_norm, stawka_nad):
        self.imie = imie
        self.stawka_norm = stawka_norm
        self.stawka_nad = stawka_nad
        self._zarobki = 0

    def pracuj(self, ile_h):
        if ile_h <= 8:
            self._zarobki += ile_h * self.stawka_norm
        else:
            self._zarobki += 8 * self.stawka_norm + (ile_h - 8) * self.stawka_nad


class Kierownik(Pracownik):
    __slots__ = [
        'bonus_kier'
    ]

    def __init__(self, *, bonus_kier, **kwargs):
        super().__init__(**kwargs)
        self.bonus_kier = bonus_kier

    def pracuj(self, ile_h):
        super().pracuj(ile_h)
        if ile_h >= 10:
            self._zarobki += self.bonus_kier


class Dyrektor(Kierownik):
    __slots__ = [
        'bonus_dyr'
    ]

    def __init__(self, *, bonus_dyr, **kwargs):
        super().__init__(**kwargs)
        self.bonus_dyr = bonus_dyr

    def pracuj(self, ile_h):
        super().pracuj(ile_h)
        self._zarobki += self.bonus_dyr


# zaimplementowac klasę Kierownik, który zarabia jak Pracownik, ale DODATKOWO:
# jeżeli zostanie w pracy co najmniej 10h to dostanie bonus

# zaimplementować:
# klasa Dyrektor która zarabia jak Kierownik i dodatkowo
# za każde wywołanie metody pracuj dostaje bonus dyrektora

# napisać funkcję zatrudnij_zespół
# polecam paczka faker
class ZatrudnijZespol:
    def __call__(self,ile_p, ile_k, ile_d):
        f = faker.Faker('PL_pl')
        lista_p = []
        for _ in range(ile_p):
            lista_p.append(Pracownik(imie=f.first_name(),
                                     stawka_norm=20,
                                     stawka_nad=40))

        for _ in range(ile_k):
            lista_p.append(Kierownik(imie=f.first_name(),
                                     stawka_norm=20,
                                     stawka_nad=40,
                                     bonus_kier=300))
        for _ in range(ile_d):
            lista_p.append(Dyrektor(imie=f.first_name(),
                                    stawka_norm=20,
                                    stawka_nad=40,
                                    bonus_kier=300,
                                    bonus_dyr=1000))
        return lista_p

zatrudnij_zespol = ZatrudnijZespol()

# def zatrudnij_zespol(ile_p, ile_k, ile_d):
#     f = faker.Faker('PL_pl')
#     lista_p = []
#     for _ in range(ile_p):
#         lista_p.append(Pracownik(imie=f.first_name(),
#                                  stawka_norm=20,
#                                  stawka_nad=40))
#
#     for _ in range(ile_k):
#         lista_p.append(Kierownik(imie=f.first_name(),
#                                  stawka_norm=20,
#                                  stawka_nad=40,
#                                  bonus_kier=300))
#     for _ in range(ile_d):
#         lista_p.append(Dyrektor(imie=f.first_name(),
#                                 stawka_norm=20,
#                                 stawka_nad=40,
#                                 bonus_kier=300,
#                                 bonus_dyr=1000))
#     return lista_p


if __name__ == '__main__':
    # p1 = Pracownik_Abstract()
    lista_p = zatrudnij_zespol(10, 3, 1)
    pprint(lista_p)
    print(lista_p[0])
    print('str', str(lista_p[0]))
    print('repr', repr(lista_p[0]))
    print('str listy', str(lista_p))
    # for p in lista_p:
    #     p.pracuj(0)
    #     p.pracuj(4)
    #     p.pracuj(8)
    #     p.pracuj(9)
    #     p.pracuj(11)
    # f_plac = sum(p.wyplata() for p in lista_p)
    # print(f_plac)

# p = Kierownik(imie='Jan',
#               stawka_norm=20,
#               stawka_nad=40,
#               bonus_kier=200)
# p.pracuj(2)  # naliczy się 40, w sumie 40
# p.pracuj(8)  # naliczy się 160, w sumie 200
# p.pracuj(9)  # naliczy się 200, w sumie 400
# p.pracuj(12)  # naliczy się 8 * 20 + 4 * 40 + 200
# print(p.wyplata())  # 920
# print(p.wyplata())  # 0
