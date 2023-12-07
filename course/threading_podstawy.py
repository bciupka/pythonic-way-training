import threading
import time

d = {}

def f1(n):
    print(f'Startuje {threading.current_thread().name}\n', end='')
    time.sleep(n)
    print(f'Koncze {threading.current_thread().name}\n', end='')
    d[threading.current_thread().name] = 'wynik'

t1 = threading.Thread(target=f1, args=(3,))
t2 = threading.Thread(target=f1, args=(3,))
t3 = threading.Thread(target=f1, args=(3,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(d)