a=int(input())
for b in range (1,a+1):
    c=int(input())
    f=[]
    for d in range(1,c+1):
        e=input()
        f.append(e)
    h=0
    for g in f:
        h=h+1
        if g=="porque":
            break
    print(h-1)