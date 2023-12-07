# napisać c3 jako funcje z yield
# dodajmy parametr do generatora filtrującego - znak komentarza

def filtruj_komentarze(g, znak='#'):
    for linia in g:
        if not linia.strip().startswith(znak):
            yield linia


def doklej_datetime(g):
    for linia in g:
        yield f'{dt.datetime.now()} {linia}'


def numeruj(g):
    for i, linia in enumerate(g):
        yield f'{i} {linia}'


import datetime as dt

if __name__ == '__main__':
    with open('c1.py', 'rt', encoding='utf8') as f, open('c1.py.out', 'wt', encoding='utf8') as f_out:
        g1 = filtruj_komentarze(f)
        g2 = doklej_datetime(g1)
        g3 = numeruj(g2)
        for linia in g3:
            f_out.write(linia)
