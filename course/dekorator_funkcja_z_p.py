import functools


def dekorator(p1, p2):
    def dekorator_wlasciwy(f):
        @functools.wraps(f)
        def nowa_f(*args, **kwargs):
            print('parametry dekoratora:', p1, p2)
            print(f'Przed wywołaniem funkcji {f} z parametrami:', args, kwargs)
            r = f(*args, **kwargs)
            print(f'Po wywołaniu funkcji {f} w zwrócona:', r)
            return r

        return nowa_f

    return dekorator_wlasciwy