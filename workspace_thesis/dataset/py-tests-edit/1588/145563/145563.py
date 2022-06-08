casos = int(input())
for i in range(casos):
    cn=int(input())
    s=0
    if 1<=cn <=10000:
        l=[int(x)for x in input().split()]
        if len(l)==cn:
            for j in range(0,len(l)):
                if l[j]%3==0:
                    s=s+l[j]
            print("La suma es",s*2)
