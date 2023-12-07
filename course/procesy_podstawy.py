import multiprocessing
import time

d = {'ala': 33}

def f1(n):
    print(f'Startuje {multiprocessing.current_process().name}\n', end='')
    time.sleep(n)
    print(f'Koncze {multiprocessing.current_process().name}\n', end='')
    print(d)
    d[multiprocessing.current_process().name] = 'wynik'

if __name__ == '__main__':
    t1 = multiprocessing.Process(target=f1, args=(3,))
    t2 = multiprocessing.Process(target=f1, args=(3,))
    t3 = multiprocessing.Process(target=f1, args=(3,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print(d)