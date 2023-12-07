import functools

@functools.lru_cache()
def fibo(n):
    # 1 1 2 3 5 8 13 21 ...
    if n < 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(492))

def do_potegi(podstawa, wykladnik):
    print('do_potegi', podstawa, wykladnik)
    return podstawa ** wykladnik

do_kwadratu = functools.partial(do_potegi, wykladnik=2)
print(do_kwadratu(5))
