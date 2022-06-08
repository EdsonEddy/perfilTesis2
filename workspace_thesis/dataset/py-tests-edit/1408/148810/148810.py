def contar(x,y):
    con=0
    c=0
    ta=len(y)-1
    for i in x:
        if con<=ta:
            if i==y[con]:
                c=c+1
        else:
            con=0
            if i==y[con]:
                c=c+1
        con=con+1
    return c
n=int(input())
r=input()
al=['A','B','C']
ed=['B','A','B','C']
ga=['C','C','A','A','B','B']
c1=contar(r,al)
c2=contar(r,ed)
c3=contar(r,ga)
v=[]
v.insert(0,int(c1))
v.insert(1,int(c2))
v.insert(2,int(c3))
v.sort()
print(v[2])
if c1==v[2]:
    print('Alvaro')
if c2==v[2]:
     print('Edwin')
if c3==v[2]:
    print('Gabriel')