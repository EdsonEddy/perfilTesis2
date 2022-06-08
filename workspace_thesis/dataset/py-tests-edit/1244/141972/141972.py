n=int(input())
for i in range(n):
    l=list(map(str,input().split()))
    if l[0]=='rectangle':
        sa=float(l[1])*float(l[2])
        print ("{0:.2f}".format(sa))
    elif l[0]=='circle':
        pi=3.14159265359
        sa=pi*float(l[1])**2
        print("{0:.2f}".format(sa))