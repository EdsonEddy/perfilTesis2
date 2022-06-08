s = input()
m = len(s)
l=[]
v =" "
for i in range(0,m,1):
    v = s[i:]
    l.append(v)
l.sort()
for i in l:
    print(i)