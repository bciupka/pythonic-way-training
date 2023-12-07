from pprint import pprint

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = []
for i in x:
    y.append(i ** 2)
y = [i ** 2 for i in x]
print(y)

y = []
for i in x:
    if i % 2 == 0:
        y.append(i ** 2)

y = [i ** 2
     for i in x
     if i % 2 == 0]
print(y)

wiersze = '12345678'
kolumny = 'abcdefgh'
y = []
for w in wiersze:
    for k in kolumny:
        y.append(f'{k}{w}')

print(y)
y = [f'{k}{w}'
     for k in kolumny
     for w in wiersze]
print(y)
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = []
for wiersz in x:
    for i in wiersz:
        y.append(i)
y = [i for wiersz in x for i in wiersz]
print(y)

tabliczka = []
for i in range(1, 7):
    wiersz = []
    for j in range(1, 5):
        wiersz.append(i * j)
    tabliczka.append(wiersz)
pprint(tabliczka)
tabliczka = [[i * j for j in range(1, 5)] for i in range(1, 7)]
pprint(tabliczka)
# użyć comprehension

x = 'ala alicja alina tomek'
# użyć comprehsion to stworzenie listy odpowiedzi na pytanie:
# czy slowo konczy sie na 'a'
# użyć takiej listy w funkcja all(), any()
y = [slowo.endswith('a') for slowo in x.split()]
print(y)
print(all(y))
print(any(y))
print(all(slowo.endswith('a') for slowo in x.split()))
print(any(slowo.endswith('a') for slowo in x.split()))

# set complehension
x = [1, 2, 5, 2, 6, 5, 7, 6, 5, 9, 11]
# zbiór reszt z dzielenia przez 5
s = {i % 5 for i in x}
print(s)

# dict comprehansion
d = {i: i % 5 
     for i in x}
print(d)

# import itertools
# print(list(itertools.product(wiersze, kolumny)))
