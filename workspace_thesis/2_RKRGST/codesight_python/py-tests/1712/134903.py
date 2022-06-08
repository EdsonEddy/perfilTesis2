n = 78
while n != 'fin':
    n = (input())
    suma = 0
    if n == 'fin':
        n = n
    else:
        for i in range(int(n)):
            suma += int(input())
        print(suma)