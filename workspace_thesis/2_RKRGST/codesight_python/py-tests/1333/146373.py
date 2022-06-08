s=input()
g=[]
for i in range(len(s)):
    x=s[i:]
    g.append(x)
g.sort()
for k in g:
    print(k)