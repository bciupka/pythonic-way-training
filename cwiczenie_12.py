# Napisać dekorator logujący wywołania
import functools
import logging


logging.basicConfig(filename='moj.log',
                    filemode='wt',
                    encoding='utf8',
                    level=logging.DEBUG)

# class dekorator:
#     def __init__(self, p1=11):
#         self.p1 = p1
#         # self.p2 = p2
#         ...
#
#     def __call__(self, f):
#         @functools.wraps(f)
#         def nowa_f(*args, **kwargs):
#             print('parametry dekoratora:', self.p1, self.p2)
#             print(f'Przed wywołaniem funkcji {f} z parametrami:', args, kwargs)
#             r = f(*args, **kwargs)
#             print(f'Po wywołaniu funkcji {f} w zwrócona:', r)
#             return r
#
#         return nowa_f

class DekoratorLogujacy:
    def __init__(self, ok_level, error_level):
        self.ok_level = ok_level
        self.error_level = error_level

    def __call__(self, f):
        @functools.wraps(f)
        def new_f(*args, **kwargs):
            lgr = logging.getLogger(__name__)
            lgr.log(self.ok_level, f'{f.__name__} ({args}')
            try:
                r = f(*args, **kwargs)
            except BaseException as e:
                lgr.log(self.error_level, f'{f.__name__}')
                raise
            else:
                lgr.log(self.ok_level, f'{f.__name__} ({args}')
                return r

        return new_f


@DekoratorLogujacy(ok_level=logging.DEBUG, error_level=logging.ERROR)
def f1(x, y):
    return x / y

if __name__ == '__main__':
    f1(1, 6)
    f1(4, 0)