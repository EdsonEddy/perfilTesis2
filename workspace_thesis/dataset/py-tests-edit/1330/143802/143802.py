cad,x=input().split(" ")
x=int(x)
n=len(cad)
a=n-x
b=cad[a:n]
c=cad[0:a]
print(b+c)