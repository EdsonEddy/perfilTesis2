x=str(input())
l=[]
for i in range(len(x)):
    l.append(x[i:])
l.sort()
for i in range(len(l)):
    print(l[i])
