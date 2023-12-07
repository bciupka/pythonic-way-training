x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = []
for wiersz in x:
    for i in wiersz:
        y.append(i)

print(y)

z = []
[z.append(i) for wiersz in x for i in wiersz]
print(z)


x = 'ala alicja alina tomek'
y = []
[y.append(i.endswith('a')) for i in x.split()]
print(any(y))
print(all(y))
print(y)
# użyć comprehsion to stworzenie listy odpowiedzi na pytanie:
# czy slowo konczy sie na 'a'
# użyć takiej listy w funkcja all(), any()