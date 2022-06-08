n=0
while n!="":
    n=int(input())
    v=input().split()
    s=input().split()
    k=0
    for i in range(len(v)):
        x=int(v[i])+int(s[i])
        k=k+x
    y=k/n
    a=0
    for g in range(len(v)):
        l=int(v[g])+int(s[g])
        if l<y:
            a=a+1
    print(a)