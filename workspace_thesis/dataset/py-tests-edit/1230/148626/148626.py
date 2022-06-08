a=int(input())
h=a//3600
a%=3600
m=a//60
a%=60
print(h,m,a)