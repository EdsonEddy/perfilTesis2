import sys
for i in sys.stdin:
    n = int(i)
    suma = 0 
    for j in range (n):
        a = int(input())
        suma = suma + a
    print(suma)