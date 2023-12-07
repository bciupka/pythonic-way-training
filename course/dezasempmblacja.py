import dis


def f1(x, y):
    z = x + y
    return z - 9


dis.dis(f1)
