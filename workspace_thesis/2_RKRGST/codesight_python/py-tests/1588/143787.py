c=int(input())
for i in range(c):
    s=0
    a=int(input())
    l=input().split()
    for j in range (a):
        if (int(l[j])*2)%3==0:
            s=s+(int(l[j])*2)
    print("La suma es",s)