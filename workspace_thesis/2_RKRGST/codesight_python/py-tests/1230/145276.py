x=int(input ())
h=int(x/3600)
x=x-(h*3600)
m=int(x/60)
s=x-(m*60)
print(h,m,s)