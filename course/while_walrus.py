# while True:
#     imie = input('Podaj imię: ')
#     if imie == 'koniec':
#         break
#     print('Cześć', imie)
import math

# od 3.8:
while (imie := input('Podaj imię: ')) != 'koniec':
    print('Cześć', imie)

# inne zastosowania:

r = 10
h = 10
v = (s := math.pi * r * r) * h
print(s, v)
i = 1
x = [j := i + 2, k := j * 5, k - 22]
print(x)

