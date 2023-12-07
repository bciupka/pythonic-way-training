import time


class Stoper:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __enter__(self):
        self.t1 = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t2 = time.perf_counter()
        # print('__exit__', exc_type, exc_val, exc_tb)
        # return True

    def __repr__(self):
        return f'{self.nazwa}: {self.t2 - self.t1:.4f} s.'


if __name__ == '__main__':
    with Stoper('100 000 insertow') as s:
        x = []
        for i in range(100_000):
            x.insert(0, i)

    print(s)
