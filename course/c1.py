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
import collections
# komentarz

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