c=int(input())
for i in range(c):
    a=input()
    l=input().split()
    b=int(l[0])
    s1=0
    s2=0
    for j in l:
        j=int(j)
        if j<b and b>s2:
            s1=s1+1
        s2=b
        b=j
    print(s1)
