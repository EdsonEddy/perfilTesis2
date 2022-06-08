a=[]
n=input()
a=n.split(" ")
z=int(a[0])
x=int(a[1])
y=int(a[2])
v=[]
a=input()
v=a.split(" ")
v2=[]
for i in range(x,y+1):
    v2.append(v[i])
v2.reverse()
i=0
for j in range(x,y+1):
    v.pop(j)
    v.insert(j,str(v2[i]))
    i=i+1
for i in v:
    print(i)