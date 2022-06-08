cad,n=map(str,input().split(" "))
s=int(n)
a = cad[(len(cad)-s):]
b = cad[:(len(cad)-s)]
print(a+b)