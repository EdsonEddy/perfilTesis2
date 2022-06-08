n=int(input()) 
h=n//3600
x=n-(3600*h)
m=x//60
s=x-(60*m)
print(h, m, s) 