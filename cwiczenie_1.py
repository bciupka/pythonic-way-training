"""
Ćwiczenie:

1. Wczytujemy adresy email z podanego pliku tekstowego emails.txt
2. Pogrupować adresy email po domenach, jedncześnie pozbywając się duplikatów. Proponuję format:
{
'gmail.com': {'ala@gmail.com', 'ela@gmail.com'}
...
}
3. Zapisujemy adresy email do plików o nazwie pochodzącej od nazwy domeny,
   wg schematu:
   np wszystkie adresy @gmail.com mają zostać zapisane w pliku gmail.com.txt

Podpowiedzi:
 - nazwę domeny można wyciąć z adresu znajdując znak @
"""
import os
import collections


lines = []

with open(r'./emails.txt', 'r') as file:
    for i in file.readlines():
        if '@' in i:
            for j in i.split(','):
                j = j.strip('\t\n ,')
                lines.append(j)

d = collections.defaultdict(set)

for i in lines:
    j = i.split('@')
    d[j[1]].add(j[0])

print(d)


# Rozwiązanie


if __name__ == '__main__':

    d = collections.defaultdict(set)
    with open('emails.txt', 'rt', encoding='utf8') as f:
        for email in f.read().replace(',', ' ').split():
            if '@' in email:
                domena = email.split('@')[1]
                d[domena].add(email)
    print(d)
    for domena, zbior_maili in d.items():
        with open(f'{domena}.txt', 'wt', encoding='utf8') as f:
            for email in zbior_maili:
                f.write(f'{email}\n')