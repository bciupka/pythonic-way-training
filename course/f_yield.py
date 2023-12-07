def f1(n):
    y = []
    for i in range(n):
        y.append(i)
    return y


def f2(n):
    print('start generatora')
    for i in range(n):
        print('generuję', i)
        yield i
    print('koniec generatora')

g = f2(5)
for i in g:
    print('konsumuję', i)
print('już po pętli')