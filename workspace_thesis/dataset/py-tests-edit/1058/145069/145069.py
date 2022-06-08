x=int(input())
for  i in range(x):
    a=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    for j in range(len(l)):
        if j<len(l)-1:
            print(l[j],end=" ")
        else:
            print(l[j])

