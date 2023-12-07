x = 'mama'

def dodaj(x, y):
    return x + y


def odejmij(x, y):
    return x - y


odejmij = lambda x, y: x - y

d = {
    '+': dodaj,
    '-': odejmij,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

x1, op, x2 = input('Podaj wyrażenie: ').split()
x1, x2 = float(x1), float(x2)
print(d[op](x1, x2))
napis = input('Podaj wyrażenie: ')

if any(c.isalpha() for c in napis):
    print('Wyrażenieza wiera litery - niebezpieczne!')
else:
    print(eval(napis))

wyr = '2 * 5 - 2'
match wyr.split():
    case [x1, ('+' | '-' | '*' | '/') as op, x2]:
        print(x1, op, x2)
    case _:
        print('Błędne wyrażenie')

match wyr.split():
    case [x1, op, x2] if op in '*/-+':
        print(x1, op, x2)
    case _:
        print('Błędne wyrażenie')

x = wyr.split()
x[0] = float(x[0])
x[2] = float(x[2])
match x:
    case [float(x1), op, float(x2)] if op in '*/-+':
        print(x1, op, x2)
    case _:
        print('Błędne wyrażenie')

x = 'a'
match x:
    case 'a':
        print('a')
    case 'b':
        print('b')
    case 'c':
        print('c')
