import functools

# functools.reduce()
# map()
# filter()
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f1(i):
    return i ** 2


print(list(map(f1, x)))
print(list(map(lambda i: i ** 2, x)))
print(list((i ** 2 for i in x)))


def parzyste(i):
    return i % 2 == 0


print(list(filter(parzyste, x)))
print(list(filter(lambda i: i % 2 == 0, x)))
print(list((i for i in x if i % 2 == 0)))

x = [None, 22, 33, 44, 0, '']
print(list(filter(None, x)))

x = 'potrzebuje ygrekow to honorowa ogromna nadzieja'
def f1(agg, slowo):
    print(agg, slowo)
    return agg + slowo[0]

print(functools.reduce(f1, x.split(), ''))