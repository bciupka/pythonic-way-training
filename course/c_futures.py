import concurrent.futures
import random
import multiprocessing

multiprocessing.Queue

def fibo(n):
    x1 = x2 = 1
    for i in range(n - 1):
        x1, x2 = x2, x1 + x2
    return x2


def n_times_fibo(m):
    for _ in range(1000):
        x = fibo(15000)
    return 'wynik'


if __name__ == '__main__':
    dane_wejsciowe = [random.randint(5000, 10000) for _ in range(100)]
    with concurrent.futures.ProcessPoolExecutor(16) as ex:
        for w in ex.map(n_times_fibo, dane_wejsciowe):
            print(w)
