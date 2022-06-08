n=input()
v=[]
for i in range(len(n)):
    v.append(n[i:])
v.sort()
for i in v:
    print(i)