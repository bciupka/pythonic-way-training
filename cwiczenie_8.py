import time


class Stoper:
    __slots__ = ['nazwa', '_start', '_stop']

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stop = time.perf_counter()

    def __repr__(self):
        return f'Czas operacji: {self._stop - self._start}'


if __name__ == '__main__':
    s = Stoper('100 000 insertow')
    with s as alias:
        x = []
        for i in range(100_000):
            x.insert(0, i)

    print(alias)
