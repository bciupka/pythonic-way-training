# python nie chroni przed przesłanianiem symboli wbudowanych funkcji
# print = 12121
# max = 11
# min = 22
# len = 222
# end = 'asdasd'
import decimal

if 22 == 22:
    if 33 == 33:
        print('aaa')
        print('aaa')
        print('aaa')
        print('aaa')
        print('aaa')
        print('aaa')
        print('aaa')
        print('aaa')
        print('aaa')
        print('aaa')
        print('aaa')
        print('aaa')

print((-9) ** .5)
x = .1 + .2
y = .3

print(x == y)
print(abs(x - y) < 0.000001)
print(round(x, 6) == round(y, 6))
import math

print(math.isclose(x, y))
import decimal as dc

print(dc.Decimal('.1') + dc.Decimal('.2') == dc.Decimal('.3'))

# bigint
x = 999 ** 999
print(type(x))
print(x)

# skończone inty
# import numpy
# numpy.int32

x = 'mama'
x.upper()
print(x)
# sklepjanie plusami - słaby pomysł
y = 'ala' + 'ma' + 'kota' + 'i' + 'psa'

# f'{wyrazenie:format}'

szablon = 'https://api.nbp.pl/api/exchangerates/rates/{}/{}/?format=json'
url = szablon.format('a', 'chf')
dane = ('a', 'chf')
url.format(*dane)

szablon = 'https://api.nbp.pl/api/exchangerates/rates/{tabela}/{waluta}/?format=json'
url = szablon.format(tabela='a', waluta='chf')
dane = {'waluta': 'chf', 'tabela': 'a', 'cosjeszcze': 123123}
print(url.format(**dane))

x = 'mama'
y = x.upper().lower()
print(x is y)
z = 'ma' + 'ma'
print(x is z)

