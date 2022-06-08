cad,n=map(str,input().split())
t=int(n)
s=0
a=cad[len(cad)-t:]
b=cad[:len(cad)-t]
print (a+b)