q=int(input())
for i in range(q):
    x=int(input())
    c=0
    if x <=1000000:
        l=[int(e) for e in input().split()]
        if len(l)==x:
            for i in range (1,len(l)-1):
                if l[i-1]<l[i] and l[i]>l[i+1]:
                    c+=1
            print(c)