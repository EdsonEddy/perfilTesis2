from sys import stdin, stdout
cad, buff = map(str, stdin.readline().split("\n"))
n, buff = map(str, stdin.readline().split("\n"))
n = int(n)
s = 0
for i in range(n):
    x, buff = map(str, stdin.readline().split("\n"))
    x = int(x)
    s = s+ x
s = s % len(cad)
a = cad[(len(cad)-s):]
b = cad[:(len(cad)-s)]
stdout.write(a+b+"\n")