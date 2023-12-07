# na bazie c1:
# wywalamy linia z wieloma emailami
# dodajemy duże litery do emails.txt
# 1. Zaczytuje emaile linai po linii
# 2. Zamienia znaki na małe litery
# 3. Odfiltrowuje puste linie i błędnyadresemail
# 4. Robi agregację do słownika zbiorów
# używamy map, filter, reduce
import collections
import functools

if __name__ == '__main__':

    d = collections.defaultdict(set)
    with open('emails.txt', 'rt', encoding='utf8') as f:
        def f1(linia):
            return linia.strip().lower()


        e1 = map(f1, f)
        e1 = map(lambda linia: linia.strip().lower(), f)

        def f2(linia):
            return '@' in linia


        e2 = filter(f2, e1)
        e2 = filter(lambda linia: '@' in linia, e1)

        def f3(d, email):
            d[email.split('@')[1]].add(email)
            return d


        functools.reduce(f3, e2, d)

        # if '@' in email:
        #     domena = email.split('@')[1]
        #     d[domena].add(email)

    print(d)
    for domena, zbior_maili in d.items():
        with open(f'{domena}.txt', 'wt', encoding='utf8') as f:
            for email in zbior_maili:
                f.write(f'{email}\n')

