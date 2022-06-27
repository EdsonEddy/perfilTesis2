import sys

cin=sys.stdin
dummy=cin.readline()
for line in cin:
    n,k=line.strip().split()
    k=int(k)
    n=n[::-1]
    v=[]
    for i in range(0,len(n)-k+1):
        s=10
        xa=n[i:i+k]
        while s>9:
            s=0
            for j in xa: s+=ord(j)-ord('0')
            xa=str(s)
        v.append(s)
    v.reverse()
    flag=0
    for i in v:
        if i==0 and flag: print(0, end='')
        elif i!=0:
            print(i,end='')
            flag=1
    print()

