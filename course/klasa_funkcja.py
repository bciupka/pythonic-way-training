class JestemKlasaAUdajeFunkcje:
    def __call__(self, *args, **kwargs):
        print('__call__', args, kwargs)


i = JestemKlasaAUdajeFunkcje()
i(11, 22, 33, p=99, k=77)
