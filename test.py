def f10():
    x = 999
    y = 888
    lista_f = []
    for z in range(3):
        def f10_1():
            print(x, y, z)

        lista_f.append(f10_1)
    return lista_f


lista_f = f10()
for f in lista_f:
    f()
print(lista_f[0].__closure__)
# print(lista_f[0].__closure__[2].cell_contents)
# print(lista_f[1].__closure__[2].cell_contents)
# print(lista_f[2].__closure__[2].cell_contents)