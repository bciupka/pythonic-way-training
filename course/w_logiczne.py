import math
x = None
if x and x.isupper():
    print(True)
else:
    print(False)

print(22 and 55)
print(22 and 0)
print(0 and '')
print(0 and 22)

imie = ''
imie = imie or 'NN'
imie = imie if imie else 'NN'
print(imie)