x1 = range(10_000_000)
input('stop')
x2 = (i**2 for i in x1)
input('stop')
x3 = (i/13 for i in x2)
input('stop')
for i in x3:
    print(i)
    if i > 100:
        break
