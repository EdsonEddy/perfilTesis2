n=int(input())
f=1
while n>1: 
    x=input().split()
    v=len(x)
    f=x[v-1]
    c=x.count(f)
    print(c)
    n=int(input())