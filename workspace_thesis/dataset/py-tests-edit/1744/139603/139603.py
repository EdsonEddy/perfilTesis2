n=int(input())
nn=n
tt=" "
for i in range (n):
    for j in range (nn):
        j=j+1
        print(j,end="")

    if(i>0):
        for t in range (i*2-1):
            print(" ",end="")

    while j!=0:
        if(j!=n):
            print(j,end="")

        j = j - 1
    print()
    nn=nn-1