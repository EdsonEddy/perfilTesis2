from sys import stdin,stdout
cad,x=map(str,stdin.readline().split(" "))
x=int(x)
n=1
suma=0
for i in range(n):
    suma+=x
suma=suma%(len(cad))
a=cad[(len(cad)-suma):]
b=cad[:(len(cad)-suma)]
stdout.write(a+b+"\n")