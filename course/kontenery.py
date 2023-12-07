# import collections
# import time
# x = []
# t1 = time.perf_counter()
# for i in range(25000):
#     x.insert(0, i)
# print(time.perf_counter() - t1)
#
# x = []
# t1 = time.perf_counter()
# for i in range(50000):
#     x.insert(0, i)
# print(time.perf_counter() - t1)
#
# x = []
# t1 = time.perf_counter()
# for i in range(100000):
#     x.insert(0, i)
# print(time.perf_counter() - t1)
#
# x = []
# t1 = time.perf_counter()
# for i in range(200000):
#     x.insert(0, i)
# print(time.perf_counter() - t1)
#
#
# x = collections.deque()
# t1 = time.perf_counter()
# for i in range(200000):
#     x.insert(0, i)
# print(time.perf_counter() - t1)

r = ['ala', 45, 56, 177]
imie, wiek, waga, wzrost = r

x = 23
y = 12
x, y = y, x
r = ['ala', 45, 56, 177]
r1 = [*r, 'Kraków']
r2 = [*r1, 'Polska']
lr = [r, r1, r2]
print(lr)

for r in lr:
    imie, wiek, waga, wzrost, *reszta = r
    print(imie, wiek , waga, wzrost, reszta)

for imie, wiek, waga, wzrost, *_ in lr:
    print(imie, wiek, waga, wzrost)

imie, *_, kraj = r2

k = (1, 2, 3)
# krotki zawierające obiekty mutowalne - zły styl

k1 = ([], [])
k1[0].append(1)
k1[0].append(2)
k1[0].append(3)
print(k1)

