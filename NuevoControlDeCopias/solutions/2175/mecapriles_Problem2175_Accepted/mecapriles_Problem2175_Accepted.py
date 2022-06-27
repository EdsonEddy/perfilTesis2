t1=[]
c=-1
v=1
e=0
for i in range(int(50)):
    e=c+v
    c=v
    v=e
    t1.append(e)
for e in range(int(input())):
    n = int(input())
    print(t1.index(n))
