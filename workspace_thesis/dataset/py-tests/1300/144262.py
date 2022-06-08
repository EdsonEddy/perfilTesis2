
n=int(input())
f=0
while n>0: 
    x=input().split() 
    v=len(x) 
    f=x[v-1]
    c=x.count(f)
    print(c) 
    n=int(input())