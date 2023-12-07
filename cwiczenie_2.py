# na bazie c1:
# wywalamy linia z wieloma emailami
# dodajemy duże litery do emails.txt
# 1. Zaczytuje emaile linai po linii
# 2. Zamienia znaki na małe litery
# 3. Odfiltrowuje puste linie i błędnyadresemail
# 4. Robi agregację do słownika zbiorów
# używamy map, filter, reduce

import functools
import collections

if __name__ == '__main__':


    def f0(line):
        return line.strip().lower()

    def f1(line):
        return '@' in line

    def f2(d, adress):
        core, mail = adress.split('@')
        return (mail, core.lower())

    d = collections.defaultdict(set)
    with open('emails.txt', 'rt', encoding='utf8') as f:
        e1 = map(f0, f)
        print(list(e1))
        e2 = filter(lambda linia: '@' in linia, e1)
        print(list(e2))
        e3 = functools.reduce(f2, e2, d)

    # print(list(e1))
    # for domena, zbior_maili in d.items():
    #     with open(f'{domena}.txt', 'wt', encoding='utf8') as f:
    #         for email in zbior_maili:
    #             f.write(f'{email}\n')