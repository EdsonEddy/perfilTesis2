cas=int(input())
while cas>0:
    n=input()
    x=tuple(map(int,input().split()))
    new=list(x)
    new.sort()
    for i in range(len(new)-1):
        print(new[i],end=" ")
    print(new[len(new)-1])
    cas-=1