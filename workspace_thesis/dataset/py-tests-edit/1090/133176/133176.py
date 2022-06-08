a=int(input())
x=0
for i in range(1,a,1):
    s=a-1
    if(s%3)==0:
        x=x+s
    a=s
print(x)