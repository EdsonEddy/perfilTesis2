cad,n= map(str,input().split(" "))
n=int(n)
a= cad[(len(cad)-n):]
b= cad[:(len(cad)-n)]
print(a+b)
