class Spychacz:
    __slots__ = ['rej', 'kier', 'akt', 'kord']

    def __init__(self, rej):
        self.rej = rej
        self.kier = ((0, 1), (1, 0), (0, -1), (-1, 0))
        self.akt = 0
        self.kord = [0, 0]

    def jedz(self, ile):
        self.kord[0] += (self.kier[self.akt][0] * ile)
        self.kord[1] += (self.kier[self.akt][1] * ile)

    def skrec_w_prawo(self):
        if self.akt > 3:
            self.akt = 0
        else:
            self.akt += 1

    def wypisz(self):
        print(f"Spychacz {self.rej} w {self.kord}")


if __name__ == '__main__':
    s = Spychacz('kr12345')
    s.wypisz()  # Spychacz kr12345 w (0, 0)
    s.jedz(10)
    s.wypisz()  # Spychacz kr12345 w (0, 10)
    s.skrec_w_prawo()
    s.jedz(10)
    s.wypisz()  # Spychacz kr12345 w (10, 10)
    s.skrec_w_prawo()
    s.jedz(10)
    s.wypisz()  # Spychacz kr12345 w (0, 10)
    s.skrec_w_prawo()
    s.jedz(10)
    s.wypisz()  # Spychacz kr12345 w (0, 0)