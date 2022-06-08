cad,x=input().split(" ")
x=int(x)
n=len(cad)
#suma=str(suma)
#alm=str(alm)
#a=1
#for i in range(x-1):
#    suma=suma+cad[n-a]
#    a=a+1
a=n-x
b=cad[a:n]
c=cad[0:a]
print(b+c)