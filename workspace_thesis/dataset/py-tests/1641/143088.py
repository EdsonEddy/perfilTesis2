from sys import stdin,stdout
c,buff = map(str, stdin.readline().split('\n'))
n,buff = map(str, stdin.readline().split('\n'))
n = int(n)
suma = 0
for i in range(n):
   x,buff = map(str, stdin.readline().split('\n'))
   x = int(x)
   suma+=x
suma = suma%len(c)
a = c[(len(c)-suma):]
b = c[:(len(c)-suma)]
stdout.write(a+b+'\n')