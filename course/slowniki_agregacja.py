x = 'ala ala ola ala ola ula'
# wynik:
{
    'ala': 3,
    'ola': 2,
    'ula': 1,
}

# policzyć to na piechotę
# 1. na piechotę
d = {}
for imie in x.split():
    # jak nie było
    if imie not in d:
        d[imie] = 1
    # a jak już było
    else:
        d[imie] = d[imie] + 1
print(d)
# 2. .get
d = {}
for imie in x.split():
    d[imie] = d.get(imie, 0) + 1
print(d)

# 3. .get
import collections


def f1():
    return 0


d = collections.defaultdict(f1)
for imie in x.split():
    d[imie] += 1
print(d)

d = collections.defaultdict(lambda: 0)
for imie in x.split():
    d[imie] += 1
print(d)

d = collections.defaultdict(int)
for imie in x.split():
    d[imie] += 1
print(d)

d = {}
for imie in x.split():
    try:
        d[imie] += 1
    except KeyError:
        d[imie] = 1
print(d)

# można ale chyba iterujemy 2 razy
d = dict.fromkeys(x.split(), 0)
for imie in x.split():
    d[imie] += 1
print(d)

x = 'ala alina alicja bartek beata'
{
    'a': ['ala', 'alina', 'alicja'],
    'b': ['bartek', 'beata']
}

d = {}
for imie in x.split():
    pl = imie[0]
    if pl not in d:
        d[pl] = []
    d[pl].append(imie)
print(d)

d = {}
for imie in x.split():
    pl = imie[0]
    lista = d.get(pl, [])
    lista.append(imie)
    d[pl] = lista
print(d)

d = collections.defaultdict(list)
for imie in x.split():
    d[imie[0]].append(imie)

print(d)

d = {}
for imie in x.split():
    d.setdefault(imie[0], []).append(imie)
print(d)
