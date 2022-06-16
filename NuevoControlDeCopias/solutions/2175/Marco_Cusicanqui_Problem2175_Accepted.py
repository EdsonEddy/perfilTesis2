import sys

cin=sys.stdin
dummy=cin.readline()
v=[]
for line in cin:
    x=int(line)
    pos=0
    a,b=0,1
    while True:
        curr=a
        if curr==x:
            print(pos)
            break
        a,b=b,a+b
        pos+=1

