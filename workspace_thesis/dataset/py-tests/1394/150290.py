l=[2,3,5,7]
c1=0
x=int(input())
for i in range (0,x):
    s= int (input())
    c=0
    sp=0
    d=0
    while s!=0:
        d=s%10
        s=s//10
        if d in l:
            c=c+1
            sp=sp+d
    if c>=3:
        if(sp%2)==0:
            c1=c1+1
print(c1)