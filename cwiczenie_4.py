# wczytywać linie z pliku tekstowego
# poddać je kolejnym przekształceniom napisanym jako ryważenia generatorowe
# 1. fitrowanie - uwuwamy linie z komentarzem #
# 2. na początku linii wklajamy aktualny datetime
# 3. na początku linii wklejamy nr kolejny
# wypisujemy przekształcone linie na ekran

import datetime as dt


# if __name__ == '__main__':
    # with open('cwiczenie_3.py', 'r') as f:
    #     g1 = (linia for linia in f if '#' not in linia)
    #     # print(list(g1))
    #     g2 = (f'{datetime.datetime.now()} {linia}' for linia in g1)
    #     # print(list(g2))
    #     g3 = (f'{i+1} {linia}' for i, linia in enumerate(g2))
    #     for linia in g3:
    #         print(linia)


if __name__ == '__main__':

    def f1(f, znak):
            for linia in f:
                if not linia.strip().startswith(znak):
                    yield f'{dt.datetime.now()} {linia}'

    def f2(g):
        for i, linia in enumerate(g):
            yield f'{i} {linia}'

    with open('cwiczenie_3.py', 'rt', encoding='utf8') as f:
        g1 = f1(f, '#')
        g2 = f2(g1)
        for i in g2:
            print(i)