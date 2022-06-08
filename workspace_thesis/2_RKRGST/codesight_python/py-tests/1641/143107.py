from sys import stdin,stdout
cad,buff = map(str, stdin.readline().split('\n'))
n,buff = map(str, stdin.readline().split('\n'))
n = int(n)
suma = 0
for i in range(n):
     x,buff = map(str, stdin.readline().split('\n'))
     x = int(x)
     suma+=x
suma = suma % len(cad)
a = cad[(len(cad)-suma):]
b = cad[:(len(cad)-suma)]
stdout.write(a + b + '\n')
