# napisać dejkorator, który zamienia wartość zwracaną przez funkcję:
# jeżeli się uda to na int
# jak sie nie uda na int - na float
# a jak sie nie uda to ValueError
import functools


def do_int_float(f):
    @functools.wraps(f)
    def nowa_f(*args, **kwargs):
        r = f(*args, **kwargs)
        try:
            return int(r)
        except ValueError:
            ...
        return float(r)

    return nowa_f


@do_int_float
def f1(i):
    return i


if __name__ == '__main__':
    print(f1(11.0))
    print(f1('11'))
    print(f1('11.55'))
    print(f1('alalalala'))
