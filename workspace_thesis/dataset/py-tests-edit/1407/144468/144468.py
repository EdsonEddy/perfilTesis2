x=int(input())
for i in range(x):
    n=int(input())
    fg=0
    l=list(map(int,input().split()))
    for j in range(len(l)):
        if j==0:
            a=0
        elif j==len(l)-1:
            a=0
        else:
            if l[j]>l[j-1] and l[j]>l[j+1]:
                fg=fg+1
    print(fg)