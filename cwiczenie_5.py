"""

Napisać generator, który będzie zwracał wszystkie dostępne notowania waluty o podanym kodzie z API NBP:

http://api.nbp.pl

Generator będzie wczytywał dane latami (wolno wysłać zapytanie tylko o rok danych na raz) i będzie zwracał (yield)notowania w kolejności odwrotnej chronologicznie (w tył).

Format pojedynczego notowania będzie słownikiem o postaci:
{
    'code': 'USD',
	'bid': 3.3,
	'ask': 3.4,
	'effectiveDate': <tutaj obiekt date z datą notowania>
}

Proponuję skorzystać z usługi:
https://api.nbp.pl/api/exchangerates/rates/c/gbp/2012-01-01/2012-01-31/?format=json

Zwróćcie uwagę, że w URLu są zawarte: kod waluty, i obie daty.
Jak wysłać zapytanie i przeczytać odpowiedź:

r = requests.get("https://api.nbp.pl/api/exchangerates/rates/c/gbp/2012-01-01/2012-01-31/?format=json")

# Sprawdzanie statusu zapytania:
# if r.status_code != 200:
#     print('coś nie tak', r.status_code)
#     exit()

# lub:
# r.raise_for_status()

# Format JSON to po prostu zagnieżdżona struktura słowników i list, a więc np cena bid # pierwszego notowania:
j = r.json()
print(j["rates"][0]["bid"])

Możemy oczywiście po listach iterować za pomocą pętli for.

Korzystamy z pakietu requests, który trzeba ściągnąć i zainstalować.
Aby to zrobić wpisujemy w oknie Terminal w Pycharm polecenie:
pip install requests

Dodadkowo dla ambitnych napisać 3 generatory przetwarzające notowania strumieniowo:
# 1. Wyliczał spread i dodawał do notowania jako wartość dla klucza 'spread'
# 2. Wyliczał zmianę względem dnia poprzedniego (dla ceny ask) - i dodawał do notowania jako wartość dla klucza 'delta'
# 3. Generator filtrujący, który będzie puszczał dalej tylko notowania spełniające warunek:
#    wartosc bezwzględna pola o nazwie nazwa_pola >= min wartosc

Ostatecznie chciałbym mieć możliwość np znaleźć notowania USD w których spread >= 0.08 i zmiana względem dnia poprzedniego była >=0.07:

g_nbp = generatorNBP("usd")
g1 = generuj_spread(g_nbp)
g2 = generuj_delta(g1)
g3 = filtruj(g2, "spread", 0.08)
g4 = filtruj(g3, "delta", 0.07)

"""
import requests
import datetime
import itertools


def generatorNBP(waluta):
    days = 0
    while True:
        dates = ((datetime.datetime.now() - datetime.timedelta(days=days*365+365)).strftime('%Y-%m-%d'),
                 (datetime.datetime.now() - datetime.timedelta(days=days*365)).strftime('%Y-%m-%d'))
        r = requests.get('https://api.nbp.pl/api/exchangerates/rates/c/{}/{}/{}/?format=json'.format(
            waluta, *(dates[0], dates[1]))
        )
        days += 1
        if r.status_code != 200:
            break
        for i in reversed(r.json()['rates']):
            del i['no']
            i['code'] = waluta.upper()
            i['effectiveDate'] = datetime.datetime.strptime(i['effectiveDate'], '%Y-%m-%d')
            yield i


def generuj_spread(g):
    for i in g:
        i['spread'] = round(i['ask'] - i['bid'], 4)
        yield i


def generuj_delta(g):
    for i, j in itertools.pairwise(g):
        i['delta'] = round(i['ask'] - j['ask'], 4)
        yield i


def filtruj(g, attr, amount):
    for i in g:
        if abs(i[attr]) < amount:
            yield i


# przygotować daty - podpowiedź datetetime.timedelta(days=1)
# while True:
#    wyslać request
#    jeżeli 404 - koniec
#    dla każdego notowania w odwrotnej kolejności:
#         zmodyfikować notowanie
#         yield notowanie
#    przeliczyć daty


if __name__ == '__main__':
    g_nbp = generatorNBP("usd")
    g1 = generuj_spread(g_nbp)
    g2 = generuj_delta(g1)
    g3 = filtruj(g2, "spread", 0.08)
    g4 = filtruj(g3, "delta", 0.07)
    for n in g4:
        print(n)