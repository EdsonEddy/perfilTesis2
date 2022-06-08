s=str(input())
l=[]
for j in range (len(s)):
    l.append(s[j:])
c=sorted(l)
for g in c:
    print(g)