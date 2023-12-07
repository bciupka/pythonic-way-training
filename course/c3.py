# wczytywać linie z pliku tekstowego
# poddać je kolejnym przekształceniom napisanym jako ryważenia generatorowe
# 1. fitrowanie - uwuwamy linie z komentarzem #
# 2. na początku linii wklajamy aktualny datetime
# 3. na początku linii wklejamy nr kolejny
# wypisujemy przekształcone linie na ekran
import datetime as dt
if __name__ == '__main__':
    with open('c1.py', 'rt', encoding='utf8') as f, open('c1.py.out', 'wt', encoding='utf8') as f_out:
        g1 = (linia for linia in f if not linia.strip().startswith('#'))
        g2 = (f'{dt.datetime.now()} {linia}' for linia in g1)
        g3 = (f'{i} {linia}' for i, linia in enumerate(g2))
        f_out.writelines(g3)
