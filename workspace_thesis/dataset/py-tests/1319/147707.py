c=int(input())
for i in range(c):
    a=int(input())
    l=input().split()
    s,s2=0,0
    h,t=0,0
    for i in l:
        if i>l[len(l)-1]:
            max=int(i)
            break
        else:
            max=int(l[len(l)-1])
    for d in l:
        s2=s2+int(d)

    if int(l[0])+int(l[1])==max or l[0]==l[len(l)-1]:
        for j in range(len(l)):
            s=s+int(l[j])
            if s==max :
                s=0
                h=h+1
        print(max)
        
    else:
        print(s2)
