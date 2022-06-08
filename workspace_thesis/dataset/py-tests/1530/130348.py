import sys
primos='2357'
for casos in range(int(input())):
    n=input()
    c=0
    for i in n:
        if i in primos:
            print(i,end='')
            c=c+1
    if c>0:
        print()
    else:
        print(0)