v = ['','unu', 'du', 'tri', 'kvar', 'Kvin', 'ses', 'Sep', 'OK', 'Nau', 'dek']
while True:
    x = int(input())
    if x < 20:
        if x <= 10:
            print(v[x])
        else:
            print('dek '+v[x % 10])
    else:
        if x % 10 != 0:
            print(str(v[x // 10]) + 'dek ' + str(v[x % 10]))
        else:
            print(str(v[x // 10]) + 'dek')