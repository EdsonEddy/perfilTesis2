from sys import stdin

v1 = ['', 'unu', 'du', 'tri', 'kvar', 'Kvin', 'ses', 'Sep', 'OK', 'Nau']
v2 = ['', 'dek', 'dudek', 'tridek', 'kvardek', 'Kvindek', 'sesdek', 'Sepdek', 'OKdek', 'Naudek']
for x in stdin:
    n = int(x)
    if n < 10:
        print(v1[n])
    if n % 10 == 0:
        print(v2[n // 10])
    if n > 10 and (n % 10) != 0:
        print(v2[n // 10], v1[n % 10])