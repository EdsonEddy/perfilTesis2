a,b,c=map(int,input().split())
xa=str(a)
xb=str(b)
xc=str(c)
n1=xa+xb+xc
n2=xa+xc+xb
n3=xb+xa+xc
n4=xb+xc+xa
n5=xc+xa+xb
n6=xc+xb+xa
n1=int(n1)
n2=int(n2)   
n3=int(n3)   
n4=int(n4)   
n5=int(n5)   
n6=int(n6)
v=[None]*6
v[0]=n1
v[1]=n2
v[2]=n3
v[3]=n4
v[4]=n5
v[5]=n6
for i in range (0,6):
    for j in range(i+1,6):
        if v[i]<v[j]:
            aux=v[i]
            v[i]=v[j]
            v[j]=aux
z=v[0]
z=int(z)
print(z)