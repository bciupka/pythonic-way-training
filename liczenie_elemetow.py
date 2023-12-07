from collections import defaultdict


x = 'ala ala ola ala ola ula'

d = {imie: 0 for imie in x.split()}

for imie in x.split():
    d[imie] += 1

print(d)

# --------------------------------------------

x = 'ala alina alicja bartek beata'

# d = defaultdict(set)
d = defaultdict(list)

for imie in x.split():
    # d[imie[0]].add(imie)
    imie not in d[imie[0]] and d[imie[0]].append(imie)

print(d)
