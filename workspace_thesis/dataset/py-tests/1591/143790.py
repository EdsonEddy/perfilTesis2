c=int(input())
for i in range(c):
    l=[2,3,5,7]
    a=input()
    s=""
    for j in a:
        if int(j) in l:
           s=s+str(j)
    if s=="":
        print(-1)
    else:
        print(s)