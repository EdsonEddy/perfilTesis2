n=int(input())
a=n//3600
x=n-(3600*a)
b=x//60
c=x-(60*b)
print(a,b,c)